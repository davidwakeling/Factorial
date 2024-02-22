import pytest
from Factorial import app

def test_service_factorial():
  rsp = app.test_client().get("/factorial/7")
  assert rsp.status_code == 200
  assert rsp.json == {"result":5040}

@pytest.mark.parametrize("n,expected",
  [ (4,24), (5,120), (7,5040), (9,362880) ])
def test_service_factorials(n,expected):
  rsp = app.test_client().get("/factorial/"+str(n))
  assert rsp.status_code == 200 
  assert rsp.json == {"result":expected}
