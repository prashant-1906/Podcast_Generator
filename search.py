import os
import logging
import requests
from pygooglenews import GoogleNews
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

news_categories = {
    "world": "World",
    "literature": "Literature",
    "politics": "Politics",
    "technology": "Technology",
    "entertainment": "Entertainment",
    "sports": "Sports",
    "stem": "STEM",
    "education": "Education",
    "lifestyle": "Lifestyle",
    "design": "Design"
}

def get_local_news(location: str, category: str = "technology", limit: int = 5) -> str:
    try:
        gn = GoogleNews()
        search = gn.search(f"{category} news {location}")
        entries = search["entries"][:limit]
        return "\n".join(f"- {entry['title']} ({entry['published']})" for entry in entries)
    except Exception as e:
        logger.error(f"Failed to fetch news: {e}")
        return "No recent news found."

def get_weather_info(location: str) -> str:
    try:
        if not OPENWEATHER_API_KEY:
            return "Weather API key not configured."
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={"q": location, "appid": OPENWEATHER_API_KEY, "units": "metric"}
        )
        if response.status_code != 200:
            return "Unable to retrieve weather."
        data = response.json()
        desc = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        return f"{desc}, {temp}°C, Humidity: {humidity}%"
    except Exception as e:
        logger.error(f"Failed to fetch weather: {e}")
        return "No weather data available."




# import logging
# import os
# import requests
# from pygooglenews import GoogleNews
# from dotenv import load_dotenv
# load_dotenv()

# logger = logging.getLogger(__name__)

# OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

# news_categories = {
#     "world": "World",
#     "literature": "Literature",
#     "politics": "Politics",
#     "technology": "Technology",
#     "entertainment": "Entertainment",
#     "sports": "Sports",
#     "stem": "STEM",
#     "education": "Education",
#     "lifestyle": "Lifestyle",
#     "design": "Design"
# }

# def get_local_news(location: str,news_category: str, limit: int = 10) -> str:
#     """Fetch local news for a given location"""
#     try:
#         gn = GoogleNews()
#         search = gn.search(f"latest news {location}, {news_category}")
#         news_entries = search['entries'][:limit]

#         news_list = []
#         for entry in news_entries:
#             title = entry.get('title', '')
#             published = entry.get('published', '')
#             news_list.append(f"- {title} ({published})")

#         return "\n".join(news_list) if news_list else "No recent news found."
    
#     except Exception as e:
#         logger.error(f"Error fetching news for {location}: {e}")
#         return "No recent news found."

# def get_weather_info(location: str) -> str:
#     """Fetch weather information for a given location"""
#     try:
#         if not OPENWEATHER_API_KEY:
#             return "Weather API key missing."
        
#         params = {
#             "q": location,
#             "appid": OPENWEATHER_API_KEY,
#             "units": "metric"
#         }
        
#         response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
        
#         if response.status_code == 200:
#             weather_data = response.json()
#             desc = weather_data['weather'][0]['description'].capitalize()
#             temp = weather_data['main']['temp']
#             humidity = weather_data['main']['humidity']
#             return f"{desc}, Temp: {temp}°C, Humidity: {humidity}%"
#         else:
#             return "Weather information unavailable."
    
#     except Exception as e:
#         logger.error(f"Error fetching weather for {location}: {e}")
#         return "Weather information unavailable."