import pytest
import requests_mock
from testhttp_modules.action_request import RequestArguments, Request, Response


def test_get_request(requests_mock):
    # Mock the HTTP response
    mock_response = {"status_code": 200, "headers": {"Content-Type": "application/json"}, "text": "Success"}
    requests_mock.get(
        "http://example.com",
        status_code=mock_response["status_code"],
        headers=mock_response["headers"],
        text=mock_response["text"],
    )

    # Create the arguments
    arguments = RequestArguments(url="http://example.com", headers=None, method="get")

    # Instantiate and run the action
    action = Request()
    result = action.run(arguments)

    # Interprete the dict correctly if the response is serialized to a dict:
    if isinstance(result, dict):
        result = Response(**result)

    # Assert the response
    assert isinstance(result, Response)
    assert result.status_code == mock_response["status_code"]
    assert result.headers["Content-Type"] == mock_response["headers"]["Content-Type"]
    assert result.text == mock_response["text"]
