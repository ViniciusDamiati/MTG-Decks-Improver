-- mtg_cards database schema — local Postgres cache of the Scryfall oracle-cards bulk dump.
-- Reference copy of what was run manually to set up the DB; re-run to recreate from scratch.

CREATE EXTENSION IF NOT EXISTS pg_trgm;

CREATE TABLE IF NOT EXISTS cards (
    id                UUID PRIMARY KEY,
    oracle_id         UUID,
    name              TEXT NOT NULL,
    mana_cost         TEXT,
    cmc               NUMERIC,
    type_line         TEXT,
    oracle_text       TEXT,
    power             TEXT,
    toughness         TEXT,
    colors            TEXT[],
    color_identity    TEXT[],
    keywords          TEXT[],
    legalities        JSONB,
    card_faces        JSONB,
    set_code          TEXT,
    collector_number  TEXT,
    rarity            TEXT,
    edhrec_rank       INTEGER,
    released_at       DATE,
    updated_at        TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_cards_name_trgm ON cards USING GIN (name gin_trgm_ops);
CREATE INDEX IF NOT EXISTS idx_cards_oracle_text_trgm ON cards USING GIN (oracle_text gin_trgm_ops);
CREATE INDEX IF NOT EXISTS idx_cards_color_identity ON cards USING GIN (color_identity);
CREATE INDEX IF NOT EXISTS idx_cards_type_line ON cards USING GIN (type_line gin_trgm_ops);
CREATE UNIQUE INDEX IF NOT EXISTS idx_cards_oracle_id ON cards (oracle_id);
