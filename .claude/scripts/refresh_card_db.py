"""Refresh the local mtg_cards Postgres database from the latest Scryfall oracle-cards bulk file.

Pulls the current download URL from the bulk-data API (so it always gets the newest dump,
no manual re-download needed) and upserts every row by oracle_id. Safe to re-run any time;
run periodically since new sets and errata land every few weeks.

Usage:
    python refresh_card_db.py
"""
import json
import os
import urllib.request

import psycopg2
import psycopg2.extras

PGPASS_PATH = r"C:\Users\vinic\.mtg-decks-improver\.pgpass"
os.environ.setdefault("PGPASSFILE", PGPASS_PATH)

H = {"User-Agent": "deck-helper/1.0", "Accept": "application/json"}

INSERT_SQL = """
INSERT INTO cards (
    id, oracle_id, name, mana_cost, cmc, type_line, oracle_text,
    power, toughness, colors, color_identity, keywords, legalities,
    card_faces, set_code, collector_number, rarity, edhrec_rank, released_at
) VALUES %s
ON CONFLICT (oracle_id) DO UPDATE SET
    name = EXCLUDED.name,
    mana_cost = EXCLUDED.mana_cost,
    cmc = EXCLUDED.cmc,
    type_line = EXCLUDED.type_line,
    oracle_text = EXCLUDED.oracle_text,
    power = EXCLUDED.power,
    toughness = EXCLUDED.toughness,
    colors = EXCLUDED.colors,
    color_identity = EXCLUDED.color_identity,
    keywords = EXCLUDED.keywords,
    legalities = EXCLUDED.legalities,
    card_faces = EXCLUDED.card_faces,
    set_code = EXCLUDED.set_code,
    collector_number = EXCLUDED.collector_number,
    rarity = EXCLUDED.rarity,
    edhrec_rank = EXCLUDED.edhrec_rank,
    released_at = EXCLUDED.released_at,
    updated_at = now()
"""


def row_for(card):
    return (
        card.get("id"),
        card.get("oracle_id"),
        card.get("name"),
        card.get("mana_cost"),
        card.get("cmc"),
        card.get("type_line"),
        card.get("oracle_text"),
        card.get("power"),
        card.get("toughness"),
        card.get("colors"),
        card.get("color_identity"),
        card.get("keywords"),
        json.dumps(card.get("legalities")) if card.get("legalities") is not None else None,
        json.dumps(card.get("card_faces")) if card.get("card_faces") is not None else None,
        card.get("set"),
        card.get("collector_number"),
        card.get("rarity"),
        card.get("edhrec_rank"),
        card.get("released_at"),
    )


def bulk_download_url():
    req = urllib.request.Request("https://api.scryfall.com/bulk-data/oracle-cards", headers=H)
    with urllib.request.urlopen(req) as r:
        meta = json.load(r)
    return meta["download_uri"], meta.get("updated_at")


def main():
    url, updated_at = bulk_download_url()
    print(f"downloading oracle-cards dump (updated_at={updated_at})\n{url}")

    conn = psycopg2.connect(host="localhost", port=5432, user="postgres", dbname="mtg_cards")
    conn.autocommit = False
    cur = conn.cursor()

    req = urllib.request.Request(url, headers=H)
    batch = []
    total = 0
    with urllib.request.urlopen(req) as r:
        for raw_line in r:
            line = raw_line.decode("utf-8").strip().rstrip(",")
            if line in ("[", "]", ""):
                continue
            try:
                card = json.loads(line)
            except json.JSONDecodeError:
                continue
            if not card.get("oracle_id"):
                continue
            batch.append(row_for(card))
            if len(batch) >= 1000:
                psycopg2.extras.execute_values(cur, INSERT_SQL, batch)
                conn.commit()
                total += len(batch)
                print(f"upserted {total}")
                batch = []

    if batch:
        psycopg2.extras.execute_values(cur, INSERT_SQL, batch)
        conn.commit()
        total += len(batch)

    print(f"done, total upserted: {total}")
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
