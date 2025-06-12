from concurrent.futures import ThreadPoolExecutor

def run_in_threads(fn, data_list):
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(fn, data_list))
    return results









# import re
# import logging

# WPM = 165

# logger = logging.getLogger(__name__)

# def count_words(text: str) -> int:
#     """Count words in text, excluding formatting"""
#     if not text:
#         return 0
#     clean_text = re.sub(r'\[ERROR\].*', '', text)
#     clean_text = re.sub(r'[*_#`]', '', clean_text)
#     clean_text = re.sub(r'\s+', ' ', clean_text)
#     words = clean_text.strip().split()
#     return len([word for word in words if word])