import logging
import os
from dotenv import load_dotenv
from langgraph.graph import StateGraph, END
from core.state import PodcastState
from processors.controller import generate_outline_and_descriptions
from processors.segment_writer import generate_segment_script
from tools.search import get_local_news, get_weather_info
from core.utils import run_in_threads
load_dotenv()

os.makedirs("logs", exist_ok=True)

log_file = "logs/podcast_debug.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(log_file, mode="a", encoding="utf-8"),
        logging.StreamHandler()  # Also print to console
    ]
)
logger = logging.getLogger(__name__)


def fetch_news_and_weather_node(state: PodcastState) -> PodcastState:
    location = state["user_address"]
    news_category = state["news_category"]
    return {
        **state,
        "local_news": get_local_news(location, news_category),
        "local_weather": get_weather_info(location)
    }

def generate_segments_node(state: PodcastState) -> PodcastState:
    topic = state["topic"]
    music_genre = state["music_genre"]
    news_weather = {
        "news": state["local_news"],
        "weather": state["local_weather"]
    }
    segments = state["segment_descriptions"]
    inputs = [(seg, topic, music_genre, news_weather) for seg in segments]
    scripts = run_in_threads(lambda args: generate_segment_script(*args), inputs)
    return {
        **state,
        "segments": scripts,
        "generation_status": "completed"
    }

def controller_node(state: PodcastState) -> PodcastState:
    episodes = generate_outline_and_descriptions(state["topic"], state["description"])
    return {**state, "segment_descriptions": episodes}

def build_podcast_graph():
    builder = StateGraph(PodcastState)

    builder.add_node("Controller", controller_node)
    builder.add_node("FetchNewsWeather", fetch_news_and_weather_node)
    builder.add_node("GenerateSegments", generate_segments_node)

    builder.set_entry_point("Controller")
    builder.add_edge("Controller", "FetchNewsWeather")
    builder.add_edge("FetchNewsWeather", "GenerateSegments")
    builder.add_edge("GenerateSegments", END)

    return builder.compile()


def run_podcast_pipeline(topic: str, duration_minutes: int, username: str, user_description: str, user_address: str, news_category: str, music_genre: str):
    logger.info("PODCAST GENERATION STARTED")
    initial_state = {
        "topic": topic,
        "description": user_description,
        "username": username,
        "user_address": user_address,
        "duration_minutes": duration_minutes,
        "news_category": news_category,
        "music_genre": music_genre,
        "research_data": "",
        "outline": "",
        "segment_descriptions": {},
        "word_allocation": {},
        "local_news": "",
        "local_weather": "",
        "segments": {},
        "word_stats": {},
        "generation_status": "starting"
    }

    graph = build_podcast_graph()
    final_state = graph.invoke(initial_state)
    logger.info("PODCAST GENERATION COMPLETED")
    return final_state


# import logging
# import os
# from langgraph.graph import StateGraph, END
# from core.state import PodcastState
# # from agents.research_agents import topic_research
# # from agents.outline_agent import generate_outline
# # from agents.planning_agent import (
# #     fetch_news_and_weather_node,
# #     calculate_word_allocation_node,
# #     generate_segment_descriptions_node
# # )
# # from agents.segment_agent import write_segments_node


# if not os.path.exists('logs'):
#     os.makedirs('logs')

# log_filename = "logs/podcast_debug.log" 

# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     handlers=[
#         logging.FileHandler(log_filename, mode='a', encoding='utf-8'),
#         logging.StreamHandler()
#     ]
# )

# logger = logging.getLogger(__name__)

# def build_podcast_graph():
#     """Build and return the podcast generation graph"""
    
#     builder = StateGraph(PodcastState)

#     builder.add_node("Research", topic_research)
#     builder.add_node("Outline", generate_outline)
#     builder.add_node("FetchNewsWeather", fetch_news_and_weather_node)
#     builder.add_node("CalculateWords", calculate_word_allocation_node)
#     builder.add_node("GenerateDescriptions", generate_segment_descriptions_node)
#     builder.add_node("WriteSegments", write_segments_node)

#     builder.set_entry_point("Research")

#     builder.add_edge("Research", "Outline")
#     builder.add_edge("Outline", "FetchNewsWeather")
#     builder.add_edge("FetchNewsWeather", "CalculateWords")
#     builder.add_edge("CalculateWords", "GenerateDescriptions")
#     builder.add_edge("GenerateDescriptions", "WriteSegments")
#     builder.add_edge("WriteSegments", END)

#     return builder.compile()

# podcast_graph = build_podcast_graph()

# def run_podcast_pipeline(topic: str, duration_minutes: int, username: str, user_description: str, user_address: str, news_category: str) -> PodcastState:
#     """Run the podcast generation pipeline"""
#     logger.info("PODCAST GENERATION STARTED")
#     logger.info(f"User: {username} | Topic: {topic} | Duration: {duration_minutes}min | Location: {user_address}")
    
#     initial_state = {
#         "topic": topic,
#         "description": user_description,
#         "username": username,
#         "user_address": user_address,
#         "duration_minutes": duration_minutes,
#         "news_category": news_category,
#         "research_data": "",
#         "outline": "",
#         "segment_descriptions": {},
#         "word_allocation": {},
#         "local_news": "",
#         "local_weather": "",
#         "segments": {},
#         "word_stats": {},
#         "generation_status": "Starting"
#     }
    
#     try:
#         final_state = podcast_graph.invoke(initial_state)
        
#         logger.info("PODCAST GENERATION COMPLETED")
#         logger.info(f"Status: {final_state.get('generation_status', 'Unknown')}")
        
#         return final_state
        
#     except Exception as e:
#         logger.error(f"pipeline failed: {e}")
#         return {"error": str(e), "segments": {}}    