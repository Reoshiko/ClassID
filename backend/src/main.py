from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.core.settings import settings
from src.routers.v1 import api_router

app = FastAPI(title="ClassID API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
