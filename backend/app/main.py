from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.resume import router as resume_router
from app.routes.job_description import router as job_description_router
from app.routes.match import router as match_router


app = FastAPI(
    title="TalentAI",
    description="Intelligent Recruitment & Resume Analysis Platform",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "TalentAI Backend is running"
    }


app.include_router(resume_router)
app.include_router(job_description_router)
app.include_router(match_router)