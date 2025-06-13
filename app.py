from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from services.podcast_generator import generate_podcast

app = FastAPI(title="Podcast Generator API")

class PodcastRequest(BaseModel):
    topic: str
    description: str = ""
    username: str 
    user_address: str
    duration: int
    news_category: str 
    music_genre: str

@app.post("/generate-podcast")
async def generate(req: PodcastRequest):
    try:
        result = generate_podcast(req.dict())
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {"message": "Podcast Generator API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)






















#  from fastapi import FastAPI, APIRouter, HTTPException
# from pydantic import BaseModel
# from core.pd_graph import run_podcast_pipeline

# router = APIRouter()

# class PodcastRequest(BaseModel):
#     topic: str
#     duration_minutes: int
#     username: str
#     user_description: str
#     user_address: str
#     news_category: str

# @router.post("/generate-podcast")
# async def generate_podcast(req: PodcastRequest):
#     try:
#         result = run_podcast_pipeline(
#             topic=req.topic,
#             duration_minutes=req.duration_minutes,
#             username=req.username,
#             user_description=req.user_description,
#             user_address=req.user_address,
#             news_category=req.news_category
#         )
#         if not result:
#             raise HTTPException(status_code=500, detail="Podcast generation failed.")
        
#         # Extract segments from result (handle both old and new format)
#         segments = result.get("segments", result) if isinstance(result, dict) else result
        
#         return {"segments": segments}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# app = FastAPI(title="Podcast Script Generator")
# app.include_router(router)

# @app.get("/")
# def root():
#     return {"message": "Podcast Generator API is running."}  # Health check

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(
#         "app:app",          
#         host="0.0.0.0",
#         port=8000,
#         reload=True
#     )