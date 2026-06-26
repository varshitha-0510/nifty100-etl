import sqlite3
import pandas as pd
import os

os.makedirs("output", exist_ok=True)

conn = sqlite3.connect("nifty100.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_key_check")

rows = cursor.fetchall()

records = []

for table, rowid, parent, fk in rows:
    records.append({
        "dq_rule": "DQ-03",
        "severity": "CRITICAL",
        "table": table,
        "rowid": rowid,
        "parent_table": parent,
        "fk_index": fk
    })

df = pd.DataFrame(records)

df.to_csv(
    "output/validation_failures.csv",
    index=False
)

print(df.head())

print(f"\nSaved {len(df)} validation failures.")

conn.close()