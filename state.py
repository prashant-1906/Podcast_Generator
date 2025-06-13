from typing import TypedDict, Dict, Any

class PodcastState(TypedDict):
    topic: str
    description: str
    username: str
    user_address: str
    duration: int
    
    research_data: str
    
    outline: str
    segment_descriptions: Dict[str, Any]
    word_allocation: Dict[str, int]
    
    local_news: str
    local_weather: str
    
    segments: Dict[str, str]
    
    word_stats: Dict[str, Dict[str, int]]
    generation_status: str