# common verification
# status code
# headers
# Data verification
# JSON Schema

def verify_status_code(response_data, expected_data):
    assert response_data.status_code == expected_data
    "Failed Test case doesnot match the status code"


def verify_response_key(key, expected_data):
    assert key == expected_data


def verify_json_key_for_not_null(key):
    assert key != 0,"Failed key is not empty" + key
    assert key >0, "Failed key is greater than zero"

def verify_json_key_for_not_null_token(key):
    assert key !=0
    "Failed key is not empty" + key

def verify_response_delete(response):
    assert "created" in response

