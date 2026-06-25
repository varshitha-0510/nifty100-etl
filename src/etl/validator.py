import pandas as pd


def load_file(file_name):
    """
    Load file with correct header handling
    """

    core_files = {
        "analysis.xlsx",
        "balancesheet.xlsx",
        "cashflow.xlsx",
        "companies.xlsx",
        "documents.xlsx",
        "profitandloss.xlsx",
        "prosandcons.xlsx"
    }

    path = f"data/raw/{file_name}"

    if file_name in core_files:
        return pd.read_excel(path, header=1)

    return pd.read_excel(path)


def check_pk_uniqueness(df, table_name, pk_column):
    """
    DQ-01: Primary Key Uniqueness
    """

    duplicates = df[df.duplicated(subset=[pk_column], keep=False)]

    if duplicates.empty:
        print(f"✅ {table_name}: PK uniqueness passed")
        return True

    print(f"❌ {table_name}: Duplicate PK found")
    print(duplicates[[pk_column]].head(10))

    return False


def check_company_year_uniqueness(df, table_name):
    """
    DQ-02: (company_id, year) uniqueness
    """

    duplicates = df[
        df.duplicated(
            subset=["company_id", "year"],
            keep=False
        )
    ]

    if duplicates.empty:
        print(f"✅ {table_name}: (company_id, year) uniqueness passed")
        return True

    print(f"❌ {table_name}: Duplicate (company_id, year) found")

    duplicate_groups = (
        duplicates.groupby(["company_id", "year"])
        .size()
        .reset_index(name="count")
    )

    print("\nActual duplicate combinations:")
    print(duplicate_groups.head(20))

    return False


def check_foreign_key_integrity(
    df,
    table_name,
    valid_company_ids
):
    """
    DQ-03: Foreign Key Integrity
    """

    invalid_rows = df[
        ~df["company_id"].isin(valid_company_ids)
    ]

    if invalid_rows.empty:
        print(f"✅ {table_name}: FK integrity passed")
        return True

    print(f"❌ {table_name}: Invalid company_id found")

    print(
        invalid_rows[["company_id"]]
        .drop_duplicates()
        .head(10)
    )

    return False


if __name__ == "__main__":

    print("\n" + "=" * 60)
    print("DQ-01: PRIMARY KEY UNIQUENESS")
    print("=" * 60)

    pk_tables = {
        "analysis.xlsx": "id",
        "balancesheet.xlsx": "id",
        "cashflow.xlsx": "id",
        "companies.xlsx": "id",
        "documents.xlsx": "id",
        "financial_ratios.xlsx": "id",
        "market_cap.xlsx": "id",
        "peer_groups.xlsx": "id",
        "profitandloss.xlsx": "id",
        "prosandcons.xlsx": "id",
        "sectors.xlsx": "id",
        "stock_prices.xlsx": "id"
    }

    for file_name, pk_column in pk_tables.items():

        df = load_file(file_name)

        check_pk_uniqueness(
            df,
            file_name,
            pk_column
        )

    print("\n" + "=" * 60)
    print("DQ-02: COMPOSITE KEY VALIDATION")
    print("=" * 60)

    year_tables = [
        "balancesheet.xlsx",
        "cashflow.xlsx",
        "financial_ratios.xlsx",
        "market_cap.xlsx",
        "profitandloss.xlsx"
    ]

    for file_name in year_tables:

        df = load_file(file_name)

        check_company_year_uniqueness(
            df,
            file_name
        )

    print("\n" + "=" * 60)
    print("DQ-03: FOREIGN KEY INTEGRITY")
    print("=" * 60)

    companies_df = load_file("companies.xlsx")

    valid_company_ids = set(
        companies_df["id"]
    )

    fk_tables = [
        "analysis.xlsx",
        "balancesheet.xlsx",
        "cashflow.xlsx",
        "documents.xlsx",
        "financial_ratios.xlsx",
        "market_cap.xlsx",
        "peer_groups.xlsx",
        "profitandloss.xlsx",
        "prosandcons.xlsx",
        "sectors.xlsx",
        "stock_prices.xlsx"
    ]

    for file_name in fk_tables:

        df = load_file(file_name)

        check_foreign_key_integrity(
            df,
            file_name,
            valid_company_ids
        )