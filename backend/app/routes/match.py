from fastapi import APIRouter, HTTPException
from app.services.job_matcher import calculate_match

router = APIRouter(
    prefix="/match",
    tags=["Resume Matching"]
)


@router.post("/")
async def match_resume_with_job(
    resume_text: str,
    job_description_text: str
):
    if not resume_text.strip():
        raise HTTPException(
            status_code=400,
            detail="Resume text cannot be empty."
        )

    if not job_description_text.strip():
        raise HTTPException(
            status_code=400,
            detail="Job description cannot be empty."
        )

    result = calculate_match(
        resume_text,
        job_description_text
    )

    return {
        "message": "Resume and Job Description matched successfully",
        **result
    }