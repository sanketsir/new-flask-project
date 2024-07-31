import pytest
import json
from app import app

def test_get_all_products():
    response = app.test_client().get('/api/products1')
    res = json.loads(response.data.decode('utf-8')).get("products1")
    assert type(res[0]) is dict
    assert type(res[1]) is dict
    assert res[0]['productName'] == 'nokia'
    assert res[0]['price'] == 80000.5
    assert response.status_code == 200
    assert type(res) is list
