"""Local Postgres lookup for the mtg_cards database (Scryfall oracle-cards dump).

Checked-in helper for deck-improvement agents/skills: query this before hitting the
live Scryfall API. Exact name match first, falling back to trigram similarity for
typos/partial names. Cards this DB doesn't have (too new, or DB not yet refreshed)
come back with "found": false — fall back to the live API pattern in CLAUDE.md for those.

Usage:
    python card_db.py "Sol Ring" "Teysa Karlov"

Prints one JSON object per line, in input order.
"""
import json
import os
import sys

import psycopg2
import psycopg2.extras

PGPASS_PATH = r"C:\Users\vinic\.mtg-decks-improver\.pgpass"
os.environ.setdefault("PGPASSFILE", PGPASS_PATH)

FIELDS = [
    "name", "mana_cost", "cmc", "type_line", "oracle_text", "power", "toughness",
    "colors", "color_identity", "keywords", "legalities", "card_faces",
    "set_code", "collector_number", "rarity", "edhrec_rank", "released_at",
]
FIELD_LIST = ", ".join(FIELDS)


def connect():
    return psycopg2.connect(host="localhost", port=5432, user="postgres", dbname="mtg_cards")


def lookup(names):
    conn = connect()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    results = []
    for name in names:
        cur.execute(
            f"SELECT {FIELD_LIST} FROM cards WHERE lower(name) = lower(%s) LIMIT 1",
            (name,),
        )
        row = cur.fetchone()
        if row is None:
            cur.execute(
                f"SELECT {FIELD_LIST} FROM cards "
                "WHERE name %% %s ORDER BY similarity(name, %s) DESC LIMIT 1",
                (name, name),
            )
            row = cur.fetchone()
        if row:
            row = dict(row)
            row["query"] = name
            row["found"] = True
        else:
            row = {"query": name, "found": False}
        results.append(row)
    cur.close()
    conn.close()
    return results


def main():
    names = sys.argv[1:]
    if not names:
        print("usage: python card_db.py <card name> [<card name> ...]", file=sys.stderr)
        sys.exit(1)
    for row in lookup(names):
        print(json.dumps(row, default=str, ensure_ascii=False))


if __name__ == "__main__":
    main()
