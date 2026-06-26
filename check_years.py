import sqlite3

conn = sqlite3.connect("nifty100.db")
cursor = conn.cursor()

company = "ABB"      # Change this to any company

tables = [
    "profitandloss",
    "balancesheet",
    "cashflow",
    "financial_ratios"
]

print(f"\nYear Coverage for {company}\n")

for table in tables:

    cursor.execute(f"""
        SELECT year
        FROM {table}
        WHERE company_id=?
        ORDER BY year
    """, (company,))

    years = [row[0] for row in cursor.fetchall()]

    print(table)
    print(years)
    print()

conn.close()