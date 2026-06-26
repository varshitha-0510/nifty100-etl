import sqlite3

conn = sqlite3.connect("nifty100.db")

cursor = conn.cursor()

tables = [
    "companies",
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

print("\nRow Counts\n")

for table in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    print(f"{table:<20} {cursor.fetchone()[0]}")

conn.close()