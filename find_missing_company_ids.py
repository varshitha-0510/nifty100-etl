import sqlite3

conn = sqlite3.connect("nifty100.db")
cursor = conn.cursor()

tables = [
    "analysis",
    "balancesheet",
    "cashflow",
    "documents",
    "financial_ratios",
    "market_cap",
    "peer_groups",
    "profitandloss",
    "prosandcons",
    "sectors",
    "stock_prices"
]

for table in tables:
    cursor.execute(f"""
        SELECT DISTINCT company_id
        FROM {table}
        WHERE company_id NOT IN (SELECT id FROM companies)
        ORDER BY company_id
    """)

    rows = cursor.fetchall()

    if rows:
        print(f"\n{table}")
        for r in rows:
            print(" ", r[0])

conn.close()