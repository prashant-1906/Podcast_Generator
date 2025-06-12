controller_prompt = """
You are a podcast planner. Create a podcast outline for the topic: {topic}.
User description: {description}

Instructions:
- Return your output strictly matching this JSON schema:
{schema}
- Include 3 to 5 episodes
- Each episode should have a clear title and 3–4 discussion points
- Structure the content for a compelling multi-episode podcast series
"""









# - intro: {intro_words} words
# - discussion1: {discussion1_words} words
# - discussion2: {discussion2_words} words
# - outro: {outro_words} words """
# You are an expert podcast producer. Your job is to generate detailed segment descriptions for an upcoming podcast episode.

# The podcast topic is: "{topic}"  
# Duration: {duration_minutes} minutes  
# Location: {user_address}

# Use a warm and professional tone.

# **CRITICAL: You must respond with ONLY valid JSON. No explanations, no markdown, no additional text.**

# **Goal**: Generate a JSON object with descriptions for 4 podcast segments: intro, discussion1, discussion2, and outro.

# Each segment should:
# - Closely align with the topic and flow naturally
# - Contain a creative and logical preview of that segment
# - Be consistent with the total length and word allocation defined below

# **Word Allocation Breakdown**
# - Total Word Count: {total_word_count}

# **For the intro description only**:
# - Also include 3-4 local news headlines (summarized) and current weather at: {user_address}
# - These will be naturally blended by the scriptwriter into the podcast intro

# **Local Context Available**:
# - News: {local_news}
# - Weather: {local_weather}

# **Required JSON Output Format**:
# {{"intro": "Segment description for intro with weather/news + hook + overview", "discussion1": "Segment description outlining the first deep dive", "discussion2": "Segment description covering the next key area", "outro": "Segment description that summarizes and signs off the podcast"}}

# Return only the JSON object above with your actual segment descriptions. No other text.
# """