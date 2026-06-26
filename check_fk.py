import sqlite3

conn = sqlite3.connect("nifty100.db")

cursor = conn.cursor()

cursor.execute("PRAGMA foreign_key_check;")

rows = cursor.fetchall()

if len(rows) == 0:
    print("✅ No foreign key violations found.")
else:
    print(f"❌ {len(rows)} foreign key violations found.")
    for row in rows[:10]:
        print(row)

conn.close()