import os
import logging
import requests
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

JAMENDO_CLIENT_ID = os.getenv("JAMENDO_CLIENT_ID")

def get_music_track(genre: str = "lofi") -> str:
    try:
        if not JAMENDO_CLIENT_ID:
            return "Jamendo API key not configured."
        response = requests.get(
            "https://api.jamendo.com/v3.0/tracks",
            params={
                "client_id": JAMENDO_CLIENT_ID,
                "format": "json",
                "limit": 1,
                "tags": genre,
                "license_ccurl": "true",
                "audioformat": "mp32"
            }
        )
        if response.status_code != 200:
            return "[Play music now]"
        data = response.json()
        track_url = data["results"][0].get("audio", "[Play music now]")
        return f"[Play music now]({track_url})"
    except Exception as e:
        logger.error(f"Failed to fetch music: {e}")
        return "[Play music now]"
