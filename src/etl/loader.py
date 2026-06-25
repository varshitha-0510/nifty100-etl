from pathlib import Path
import pandas as pd

RAW_DATA_PATH = Path("data/raw")

CORE_FILES = {
    "analysis.xlsx",
    "balancesheet.xlsx",
    "cashflow.xlsx",
    "companies.xlsx",
    "documents.xlsx",
    "profitandloss.xlsx",
    "prosandcons.xlsx"
}


def load_excel_file(file_path):
    """
    Load Excel file with correct header handling.
    """

    if file_path.name in CORE_FILES:
        return pd.read_excel(file_path, header=1)

    return pd.read_excel(file_path, header=0)


def process_all_files():

    excel_files = sorted(RAW_DATA_PATH.glob("*.xlsx"))

    print(f"\nFound {len(excel_files)} Excel files\n")

    for file in excel_files:

        try:

            df = load_excel_file(file)

            print("=" * 60)
            print(f"File Name : {file.name}")
            print(f"Rows      : {len(df)}")
            print(f"Columns   : {len(df.columns)}")

            print("First 5 Columns:")
            print(df.columns.tolist()[:5])

            print()

        except Exception as e:
            print(f"Error reading {file.name}: {e}")


if __name__ == "__main__":
    process_all_files()