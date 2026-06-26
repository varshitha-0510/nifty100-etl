import sqlite3
import random

conn = sqlite3.connect("nifty100.db")
cursor = conn.cursor()

cursor.execute("SELECT id FROM companies")
companies = [row[0] for row in cursor.fetchall()]

sample = random.sample(companies, 5)

print("=" * 60)
print("Manual Review")
print("=" * 60)

for company in sample:
    print(f"\nCompany: {company}")

    for table in [
        "profitandloss",
        "balancesheet",
        "cashflow",
        "financial_ratios",
    ]:

        cursor.execute(f"""
            SELECT COUNT(*)
            FROM {table}
            WHERE company_id=?
        """, (company,))

        count = cursor.fetchone()[0]

        print(f"{table:<20} {count} rows")

conn.close()