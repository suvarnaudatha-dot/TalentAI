import os

from dotenv import load_dotenv
from supabase import create_client, Client


load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")


if not SUPABASE_URL or not SUPABASE_KEY:
    raise RuntimeError(
        "SUPABASE_URL and SUPABASE_KEY must be set in .env"
    )


supabase: Client = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)


def check_duplicate_resume(extracted_text: str) -> bool:
    """
    Check whether the same resume text already exists.
    """

    response = (
        supabase
        .table("resumes")
        .select("id")
        .eq("extracted_text", extracted_text)
        .limit(1)
        .execute()
    )

    return len(response.data) > 0


def save_resume(
    filename: str,
    content_type: str,
    extracted_text: str,
    resume_score: int,
    duplicate: bool,
    skills: list[str]
):
    """
    Save resume information and skills to Supabase.
    """

    # Save resume
    resume_response = (
        supabase
        .table("resumes")
        .insert({
            "filename": filename,
            "content_type": content_type,
            "extracted_text": extracted_text,
            "resume_score": resume_score,
            "duplicate": duplicate
        })
        .execute()
    )

    resume_id = resume_response.data[0]["id"]

    # Save skills
    if skills:
        skill_records = [
            {
                "resume_id": resume_id,
                "skill": skill
            }
            for skill in skills
        ]

        (
            supabase
            .table("resume_skills")
            .insert(skill_records)
            .execute()
        )

    return resume_id