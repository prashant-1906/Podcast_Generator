import argparse
import logging
import sys
from services.podcast_generator import generate_podcast

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description='Generate an AI-powered podcast')
    parser.add_argument('--topic', required=True)
    parser.add_argument('--description', default="")
    parser.add_argument('--username', default="User")
    parser.add_argument('--location', required=True)
    parser.add_argument('--duration', type=int, default=30)
    parser.add_argument('--news_category', default="technology")
    parser.add_argument('--music_genre', default="lofi")
    args = parser.parse_args()

    logger.info(f"Starting podcast for topic: {args.topic}")
    payload = {
        "topic": args.topic,
        "description": args.description,
        "username": args.username,
        "user_address": args.location,
        "duration": args.duration,
        "news_category": args.news_category,
        "music_genre": args.music_genre
    }
    result = generate_podcast(payload)

    if "segments" in result:
        for seg in result["segments"]:
            print(f"\n--- {seg['title']} ---\n{seg['structured_script']}\n")
    else:
        print("Error generating podcast.")

if __name__ == "__main__":
    main()



# import argparse
# import logging
# import sys
# # from pathlib import Path
# from core.pd_graph import run_podcast_pipeline

# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
# )
# logger = logging.getLogger(__name__)

# def main():
#     """Main CLI interface"""
#     parser = argparse.ArgumentParser(description='Generate AI podcast content')
    
#     parser.add_argument('--topic', required=True, help='Podcast topic')
#     parser.add_argument('--duration', type=int, required=True, help='Duration in minutes')
#     parser.add_argument('--username', default='User', help='Username')
#     parser.add_argument('--description', default='', help='Topic description')
#     parser.add_argument('--location', required=True, help='User location for local news/weather')
#     parser.add_argument('--output', default='./output', help='Output directory')
    
#     args = parser.parse_args()
    
#     # # Create output directory
#     # output_dir = Path(args.output)
#     # output_dir.mkdir(exist_ok=True)
    
#     logger.info(f"Starting podcast generation for topic: {args.topic}")
    
#     try:
#         result = run_podcast_pipeline(
#             topic=args.topic,
#             duration_minutes=args.duration,
#             username=args.username,
#             user_description=args.description,
#             user_address=args.location
#         )
        
#         if 'error' in result:
#             logger.error(f"Pipeline failed: {result['error']}")
#             sys.exit(1)
        
#         # Save output
#         segments = result.get('segments', {})
#         # output_file = output_dir / f"podcast_{args.topic.replace(' ', '_').lower()}.txt"
        
#         # with open(output_file, 'w', encoding='utf-8') as f:
#         #     f.write(f"# Podcast: {args.topic}\n")
#         #     f.write(f"Duration: {args.duration} minutes\n")
#         #     f.write(f"Location: {args.location}\n\n")
            
#         #     for segment_name, content in segments.items():
#         #         f.write(f"## {segment_name.title()}\n\n")
#         #         f.write(f"{content}\n\n")
        
#         logger.info(f"Podcast generated successfully")          # {output_file}
#         print(f"Generated segments: {list(segments.keys())}")
#         # print(f"Output saved to: {output_file}")
        
#     except Exception as e:
#         logger.error(f"Failed to generate podcast: {e}")
#         sys.exit(1)

# if __name__ == "__main__":
#     main()