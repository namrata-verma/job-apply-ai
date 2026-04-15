from fastapi import FastAPI
from api import router

app = FastAPI(
    title="Job Apply AI",
    description="AI-powered job matching and recommendation engine",
    version="0.1.0"
)

app.include_router(router)
