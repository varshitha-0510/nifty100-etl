from src.etl.normaliser import normalize_year, normalize_ticker


def test_normalize_year_fy23():
    assert normalize_year("FY23") == 2023


def test_normalize_year_four_digit():
    assert normalize_year("2023") == 2023


def test_normalize_year_range():
    assert normalize_year("2023-24") == 2023


def test_normalize_year_none():
    assert normalize_year(None) is None


def test_normalize_ticker_lowercase():
    assert normalize_ticker("tcs") == "TCS"


def test_normalize_ticker_spaces():
    assert normalize_ticker(" infy ") == "INFY"


def test_normalize_ticker_mixed_case():
    assert normalize_ticker("Hdfc Bank") == "HDFC BANK"


def test_normalize_ticker_none():
    assert normalize_ticker(None) is None