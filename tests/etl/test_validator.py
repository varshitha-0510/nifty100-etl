import pandas as pd
from src.etl.validator import check_pk_uniqueness


def test_dummy():
    df = pd.DataFrame(
        {
            "id": [1, 2, 3]
        }
    )

    check_pk_uniqueness(
        df,
        "test",
        "id"
    )