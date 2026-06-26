import sqlite3
import pandas as pd

DB_PATH = "nifty100.db"

CORE_FILES = {
    "analysis.xlsx",
    "balancesheet.xlsx",
    "cashflow.xlsx",
    "companies.xlsx",
    "documents.xlsx",
    "profitandloss.xlsx",
    "prosandcons.xlsx"
}

LOAD_ORDER = [
    ("companies.xlsx", "companies"),
    ("analysis.xlsx", "analysis"),
    ("balancesheet.xlsx", "balancesheet"),
    ("cashflow.xlsx", "cashflow"),
    ("documents.xlsx", "documents"),
    ("financial_ratios.xlsx", "financial_ratios"),
    ("market_cap.xlsx", "market_cap"),
    ("peer_groups.xlsx", "peer_groups"),
    ("profitandloss.xlsx", "profitandloss"),
    ("prosandcons.xlsx", "prosandcons"),
    ("sectors.xlsx", "sectors"),
    ("stock_prices.xlsx", "stock_prices")
]


def load_excel(file_name, table_name):
    header = 1 if file_name in CORE_FILES else 0

    df = pd.read_excel(
        f"data/raw/{file_name}",
        header=header
    )

    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    conn = sqlite3.connect(DB_PATH)

    df.to_sql(
        table_name,
        conn,
        if_exists="append",
        index=False
    )

    conn.close()

    print(f"✅ {table_name:<20} {len(df)} rows")


if __name__ == "__main__":

    print("\nLoading all Excel files...\n")

    for file_name, table_name in LOAD_ORDER:
        load_excel(file_name, table_name)

    print("\n🎉 All files loaded successfully!")