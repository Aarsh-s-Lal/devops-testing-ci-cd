import pytest
import requests

# Test cases in the format (URL, Expected Result, Description)
testcases = [
    ("http://127.0.0.1:8000/add/10/5", 15, "Addition"),
    ("http://127.0.0.1:8000/add/-3/3", 0, "Addition of negative numbers"),
]

@pytest.mark.parametrize("url, expected, description", testcases)
def test_api(url, expected, description):
    response = requests.get(url)
    assert response.status_code == 200, f"{description} FAILED! Expected status 200, got {response.status_code}"
    
    result = response.json().get("result")
    assert result == expected, f"{description} FAILED! Expected {expected}, got {result}"
