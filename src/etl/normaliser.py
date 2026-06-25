import re


def normalize_year(year):
    if year is None:
        return None

    year = str(year).strip()

    if year.startswith("FY"):
        return int("20" + year[-2:])

    if "-" in year:
        parts = year.split("-")

        if len(parts[1]) == 2:
            return int(parts[0][:2] + parts[1])

        return int(parts[1])

    match = re.search(r"\d{4}", year)

    if match:
        return int(match.group())

    return None


def normalize_ticker(ticker):
    if ticker is None:
        return None

    return str(ticker).strip().upper()