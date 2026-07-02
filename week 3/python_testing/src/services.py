import requests

from . import db


def update_user_records(user_id, email, city):
    """Dummy database function to satisfy imports during testing."""
    pass


def sync_user_profile_data(user_id: int) -> dict:

    api_url = f"https://api.example.com/v1/profiles/{user_id}"
    response = requests.get(api_url, timeout=5)

    if response.status_code != 200:
        raise RuntimeError("External API communication Failed")

    api_data = response.json()
    email_address = api_data.get("email")
    location_city = api_data.get("city")
    db.update_user_records(user_id, email=email_address, city=location_city)

    return {"status": "Synced successfully", "user_id": user_id}
