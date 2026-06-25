from pathlib import Path
import pandas as pd


RAW_DATA_PATH = Path("data/raw")


def load_excel_file(file_path):
    """
    Load an Excel file and return DataFrame.
    """

    df = pd.read_excel(file_path)

    return df


def process_all_files():
    """
    Read all Excel files from data/raw.
    """

    excel_files = list(RAW_DATA_PATH.glob("*.xlsx"))

    print(f"\nFound {len(excel_files)} Excel files\n")

    for file in excel_files:

        try:

            df = load_excel_file(file)

            print("=" * 50)
            print(f"File Name : {file.name}")
            print(f"Rows      : {df.shape[0]}")
            print(f"Columns   : {df.shape[1]}")

            print("Column Names:")
            print(df.columns.tolist())

            print()

        except Exception as e:

            print(f"Error reading {file.name}")
            print(e)


if __name__ == "__main__":
    process_all_files()