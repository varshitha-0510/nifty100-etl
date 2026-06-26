import sqlite3

conn = sqlite3.connect("nifty100.db")
cursor = conn.cursor()

cursor.execute("""
SELECT company_id,
COUNT(DISTINCT year)
FROM profitandloss
GROUP BY company_id
HAVING COUNT(DISTINCT year)<5
ORDER BY COUNT(DISTINCT year)
""")

rows = cursor.fetchall()

print("\nCompanies with less than 5 years of data\n")

for row in rows:
    print(row)

conn.close()