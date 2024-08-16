import pytest
import main
from config import URL

def test_read_data():
    """test_read_data _Function testing reading the data_
    """

    d1, d2 = main.read("customers.csv", "purchases.csv")

    assert len(d1) == 5, "Customer Dataframe length mismatch"
    assert len(d2) == 5, "PurchaseDataframe length mismatch"

def test_file_not_found():
    
    with pytest.raises(SystemExit) as e:
        main.read("customers.csv", "purcha.csv")

    # Check that it exits with code 1
    assert e.value.code == 1
