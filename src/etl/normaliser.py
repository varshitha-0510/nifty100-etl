import re


def normalize_year(year):
    if year is None:
        return None

    year = str(year).strip().upper()

    # Match 4-digit year
    match = re.search(r"(20\d{2})", year)
    if match:
        return int(match.group(1))

    # Match FY23
    match = re.search(r"FY\s?(\d{2})", year)
    if match:
        return 2000 + int(match.group(1))

    return None


def normalize_ticker(ticker):
    if ticker is None:
        return None

    return str(ticker).strip().upper()


if __name__ == "__main__":
    print(normalize_year("FY23"))
    print(normalize_year("2023"))
    print(normalize_year("2023-24"))

    print(normalize_ticker("tcs"))
    print(normalize_ticker(" infy "))