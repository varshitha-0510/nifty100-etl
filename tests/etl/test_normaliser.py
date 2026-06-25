from src.etl.normaliser import normalize_year, normalize_ticker


def test_normalize_year_fy23():
    assert normalize_year("FY23") == 2023


def test_normalize_year_four_digit():
    assert normalize_year("2018") == 2018


def test_normalize_year_range():
    assert normalize_year("2020-21") == 2021


def test_normalize_year_none():
    assert normalize_year(None) is None


def test_year_fy20():
    assert normalize_year("FY20") == 2020


def test_year_fy21():
    assert normalize_year("FY21") == 2021


def test_normalize_ticker_lowercase():
    assert normalize_ticker("abb") == "ABB"


def test_normalize_ticker_spaces():
    assert normalize_ticker(" reliance ") == "RELIANCE"


def test_normalize_ticker_mixed_case():
    assert normalize_ticker("TcS") == "TCS"


def test_normalize_ticker_none():
    assert normalize_ticker(None) is None