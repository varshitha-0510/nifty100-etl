import pandas as pd

companies = pd.read_excel(
    "data/raw/companies.xlsx",
    header=1
)

print("Total companies:", len(companies))

print("\nLast 20 company IDs:\n")

print(
    companies["id"]
    .tail(20)
    .tolist()
)