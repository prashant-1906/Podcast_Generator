from processors.controller import generate_outline_and_descriptions
from processors.segment_writer import generate_segment_script
from tools.search import get_local_news, get_weather_info
from core.utils import run_in_threads

def generate_podcast(payload):
    topic = payload["topic"]
    location = payload["user_address"]
    news_category = payload["news_category"]
    music_genre = payload["music_genre"]
    user_description = payload.get("description", "")
    duration = payload.get("duration")

    segments = generate_outline_and_descriptions(topic, user_description, duration)
    news_weather = {
        "news": get_local_news(location, news_category),
        "weather": get_weather_info(location)
    }
    inputs = [(seg, topic, music_genre, news_weather) for seg in segments]
    results = run_in_threads(lambda args: generate_segment_script(*args), inputs)
    return {"segments": results}