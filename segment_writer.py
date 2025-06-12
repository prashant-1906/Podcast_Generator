from prompts.segment_prompt import segment_prompt
from prompts.intro_prompt import intro_prompt
from core.schema import segment_output_schema

def generate_segment_script(segment, topic, music_genre, news_weather):
    prompt_template = intro_prompt if segment["title"].lower() == "intro" else segment_prompt
    prompt = prompt_template.format(
        title=segment["title"],
        description=segment["description"],
        topic=topic,
        music_genre=music_genre,
        news_weather=news_weather if segment["title"].lower() == "intro" else "",
        json_schema=segment_output_schema
    )
    return {
        "id": segment["id"],
        "title": segment["title"],
        "structured_script": prompt
    }
