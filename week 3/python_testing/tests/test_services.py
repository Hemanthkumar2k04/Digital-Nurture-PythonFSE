from unittest.mock import MagicMock, patch

import pytest
from src.services import sync_user_profile_data


@patch("src.services.db.update_user_records")
@patch("src.services.requests.get")
def test_sync_user_profile_data_happy_path(mock_get, mock_update_db):

    fake_http_response = MagicMock()
    fake_http_response.status_code = 200
    fake_http_response.json.return_value = {"email": "hk@gmail.com", "city": "Chennai"}
    mock_get.return_value = fake_http_response

    output = sync_user_profile_data(777)

    assert output["status"] == "Synced successfully"
    assert output["user_id"] == 777

    mock_get.assert_called_once_with(
        "https://api.example.com/v1/profiles/777", timeout=5
    )
    mock_update_db.assert_called_once_with(777, email="hk@gmail.com", city="Chennai")


@patch("src.services.requests.get")
def test_sync_user_profile_data_api_failure(mock_get):

    fake_http_response = MagicMock()
    fake_http_response.status_code = 500
    mock_get.return_value = fake_http_response

    with pytest.raises(RuntimeError, match="External API communication Failed"):
        sync_user_profile_data(777)
