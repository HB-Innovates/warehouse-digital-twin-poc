import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from warehouse_usd_model import create_warehouse_usd

@pytest.mark.skipif(sys.platform != "win32", reason="USD tests require Windows environment")
def test_usd_model_creation():
    filename = "test_warehouse.usda"
    result = create_warehouse_usd(filename)
    assert os.path.exists(result)
    os.remove(result)
