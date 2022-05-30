import pytest
import requests
import json

@pytest.mark.parametrize("userid, firstname",[(1,"George"),(2,"Janet")])
def test_check_user(userid, firstname) :
  url = f"https://reqres.in/api/users/{userid}"
  resp = request.get(url)
  assert resp.status_code == 200, "failed"
  jsonObj = json.loads(resp.text)
