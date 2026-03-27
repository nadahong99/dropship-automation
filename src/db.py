import sqlite3
from pathlib import Path

DB_PATH = Path("data.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS product_candidates (
        sku TEXT PRIMARY KEY,
        title TEXT,
        source_site TEXT,
        source_url TEXT,
        unit_cost_krw INTEGER,
        moq INTEGER,
        image_url TEXT,
        category TEXT
    )""")
    cur.execute("""
    CREATE TABLE IF NOT EXISTS priced_products (
        sku TEXT PRIMARY KEY,
        title TEXT,
        source_site TEXT,
        source_url TEXT,
        unit_cost_krw INTEGER,
        moq INTEGER,
        image_url TEXT,
        category TEXT,
        sell_price_krw INTEGER,
        gross_margin_pct REAL,
        moq_risk_score REAL,
        competitor_price_avg INTEGER
    )""")
    conn.commit()
    conn.close()
