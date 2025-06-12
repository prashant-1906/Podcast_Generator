from tools.search import get_local_news, get_weather_info
from core.utils import WPM

def fetch_news_and_weather(state):
    location = state["location"]
    return {
        **state,
        "news_weather": {
            "news": get_local_news(location),
            "weather": get_weather_info(location)
        }
    }

def calculate_word_allocation(state):
    minutes = state["duration_minutes"]
    total_words = int(minutes * WPM)
    return {
        **state,
        "word_allocation": {
            "intro": int(0.25 * total_words),
            "discussion1": int(0.25 * total_words),
            "discussion2": int(0.25 * total_words),
            "outro": total_words - int(0.25 * total_words) * 3,
            "total": total_words
        }
    }