from fastapi import FastAPI
from src.routers.v1 import api_router

app = FastAPI(title="ClassID API", version="1.0.0")

app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
