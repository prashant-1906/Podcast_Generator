import json
from prompts.Controller_prompt import controller_prompt
from langchain_openai import ChatOpenAI
from core.schema import podcast_outline_schema

def generate_outline_and_descriptions(topic, description):
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
    schema_str = json.dumps(podcast_outline_schema, indent=2)
    prompt = controller_prompt.format(
        topic=topic,
        description=description,
        duration="",
        schema=schema_str
    )
    response = llm.invoke(prompt)
    content = response.content.strip()

    try:
        parsed = json.loads(content)
        return parsed["episodes"]
    except Exception as e:
        raise ValueError(f"Failed to parse controller output: {e}")