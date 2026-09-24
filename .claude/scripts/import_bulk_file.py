"""Import a locally-downloaded Scryfall bulk file into the local mtg_cards Postgres database.

Unlike refresh_card_db.py (which streams the "oracle-cards" bulk dump — one row per unique
card — from the web), this script is for bulk files that have ONE ROW PER PRINTING, such as
Scryfall's "all-cards" (or "default-cards") dump: default-cards.json, all-cards.json, or a
manually-downloaded .jsonl.gz/.json/.jsonl of either. It streams the file (gzip handled without
ever decompressing to disk) and dedupes down to a single printing per oracle_id before upserting,
using the same INSERT_SQL / row_for as refresh_card_db.py.

Selection rule per oracle_id: prefer printings whose `games` includes "paper"; among paper
printings, keep the newest `released_at` (ties -> first seen). If a card has no paper printing
at all (Arena-only/digital-only card), fall back to the newest non-paper printing seen, so it
still gets a row.

Usage:
    python import_bulk_file.py <path-to-bulk-file.jsonl.gz|.json|.jsonl>
"""
import gzip
import json
import os
import sys

import psycopg2
import psycopg2.extras

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from refresh_card_db import INSERT_SQL, row_for  # noqa: E402

PGPASS_PATH = r"C:\Users\vinic\.mtg-decks-improver\.pgpass"
os.environ.setdefault("PGPASSFILE", PGPASS_PATH)


def open_stream(path):
    if path.endswith(".gz"):
        return gzip.open(path, "rt", encoding="utf-8")
    return open(path, "rt", encoding="utf-8")


def is_paper(card):
    games = card.get("games") or []
    return "paper" in games


def better(candidate, current):
    """Return True if `candidate` card should replace `current` chosen card for an oracle_id."""
    if current is None:
        return True
    cand_paper = is_paper(candidate)
    cur_paper = is_paper(current)
    if cand_paper != cur_paper:
        # prefer paper over non-paper
        return cand_paper and not cur_paper
    # same paper-ness: prefer newer released_at; ties -> keep first seen (don't replace)
    cand_rel = candidate.get("released_at") or ""
    cur_rel = current.get("released_at") or ""
    return cand_rel > cur_rel


def main():
    if len(sys.argv) != 2:
        print("usage: python import_bulk_file.py <path-to-bulk-file.jsonl.gz|.json|.jsonl>", file=sys.stderr)
        sys.exit(1)

    path = sys.argv[1]
    if not os.path.isfile(path):
        print(f"error: file not found: {path}", file=sys.stderr)
        sys.exit(1)

    print(f"scanning {path} ...")

    # oracle_id -> (chosen_row_tuple, chosen_card_meta_for_comparison)
    chosen_rows = {}
    chosen_meta = {}  # oracle_id -> {"games": [...], "released_at": "..."}

    lines_seen = 0
    skipped_no_oracle_id = 0

    with open_stream(path) as f:
        for raw_line in f:
            lines_seen += 1
            line = raw_line.strip().rstrip(",")
            if line in ("[", "]", ""):
                continue
            try:
                card = json.loads(line)
            except json.JSONDecodeError:
                continue
            oracle_id = card.get("oracle_id")
            if not oracle_id:
                skipped_no_oracle_id += 1
                continue

            current_meta = chosen_meta.get(oracle_id)
            candidate_meta = {"games": card.get("games") or [], "released_at": card.get("released_at") or ""}

            if current_meta is None:
                chosen_rows[oracle_id] = row_for(card)
                chosen_meta[oracle_id] = candidate_meta
            else:
                # reconstruct minimal "current" for comparison
                current_stub = {"games": current_meta["games"], "released_at": current_meta["released_at"]}
                candidate_stub = {"games": candidate_meta["games"], "released_at": candidate_meta["released_at"]}
                if better(candidate_stub, current_stub):
                    chosen_rows[oracle_id] = row_for(card)
                    chosen_meta[oracle_id] = candidate_meta

            if lines_seen % 100000 == 0:
                print(f"scanned {lines_seen} lines, {len(chosen_rows)} distinct oracle_ids so far")

    print(f"scan complete: {lines_seen} lines, {skipped_no_oracle_id} skipped (no oracle_id), "
          f"{len(chosen_rows)} distinct oracle_ids selected")

    conn = psycopg2.connect(host="localhost", port=5432, user="postgres", dbname="mtg_cards")
    conn.autocommit = False
    cur = conn.cursor()

    rows = list(chosen_rows.values())
    total = 0
    errors = []
    batch_size = 1000
    for i in range(0, len(rows), batch_size):
        batch = rows[i:i + batch_size]
        try:
            psycopg2.extras.execute_values(cur, INSERT_SQL, batch)
            conn.commit()
            total += len(batch)
            print(f"upserted {total}/{len(rows)}")
        except psycopg2.Error as e:
            conn.rollback()
            # fall back to per-row upsert for this batch so one bad row (e.g. an id PK
            # collision across a different oracle_id) doesn't kill the whole batch
            print(f"batch {i}-{i+len(batch)} failed as a whole ({e}); retrying rows individually")
            for row in batch:
                try:
                    psycopg2.extras.execute_values(cur, INSERT_SQL, [row])
                    conn.commit()
                    total += 1
                except psycopg2.Error as row_err:
                    conn.rollback()
                    errors.append((row[1], row[2], str(row_err).strip()))  # oracle_id, name, error

    print(f"done, total upserted: {total}")
    if errors:
        print(f"{len(errors)} rows failed to upsert:")
        for oracle_id, name, err in errors[:50]:
            print(f"  oracle_id={oracle_id} name={name!r}: {err}")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
