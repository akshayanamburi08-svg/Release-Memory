from fastapi import FastAPI
from pydantic import BaseModel

from .agent import analyze_release

app = FastAPI(
    title="Release Memory",
    description="A release-readiness agent powered by Hindsight memory.",
)


class ReleaseRequest(BaseModel):
    service: str
    environment: str
    release: str
    change: str


@app.get("/")
def health_check():
    return {
        "project": "Release Memory",
        "status": "running",
        "message": "The Hindsight-powered release analysis API is ready.",
    }


@app.post("/analyze")
def analyze(request: ReleaseRequest):
    return analyze_release(
        service=request.service,
        environment=request.environment,
        release=request.release,
        change=request.change,
    )
