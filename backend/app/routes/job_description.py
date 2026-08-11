
from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.pdf_parser import extract_text_from_pdf
from app.services.text_cleaner import clean_text
from app.services.skill_extractor import extract_skills

import os
import shutil
import tempfile

router = APIRouter(
    prefix="/job-description",
    tags=["Job Description"]
)


@router.post("/upload")
async def upload_job_description(file: UploadFile = File(...)):

    allowed_types = [
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ]

    # Validate file type
    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are allowed for Job Description."
        )

    # =========================================================
    # PDF PROCESSING
    # =========================================================

    if file.content_type == "application/pdf":

        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        )

        try:
            shutil.copyfileobj(file.file, temp_file)
            temp_file.close()

            # Step 1: Extract text
            extracted_text = extract_text_from_pdf(
                temp_file.name
            )

            # Step 2: Clean text
            cleaned_text = clean_text(
                extracted_text
            )

            # Step 3: Extract skills
            skills = extract_skills(
                cleaned_text
            )

        finally:
            if os.path.exists(temp_file.name):
                os.unlink(temp_file.name)

        return {
            "filename": file.filename,
            "content_type": file.content_type,
            "message": "Job Description uploaded, extracted, cleaned and skills extracted successfully",
            "job_description_text": cleaned_text,
            "skills": skills
        }

    # =========================================================
    # DOCX PROCESSING
    # =========================================================

    if file.content_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":

        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".docx"
        )

        try:
            shutil.copyfileobj(file.file, temp_file)
            temp_file.close()

            from docx import Document

            document = Document(temp_file.name)

            paragraphs = []

            for paragraph in document.paragraphs:
                if paragraph.text.strip():
                    paragraphs.append(
                        paragraph.text.strip()
                    )

            extracted_text = "\n".join(paragraphs)

            # Step 1: Clean extracted text
            cleaned_text = clean_text(
                extracted_text
            )

            # Step 2: Extract skills
            skills = extract_skills(
                cleaned_text
            )

        finally:
            if os.path.exists(temp_file.name):
                os.unlink(temp_file.name)

        return {
            "filename": file.filename,
            "content_type": file.content_type,
            "message": "Job Description uploaded, extracted, cleaned and skills extracted successfully",
            "job_description_text": cleaned_text,
            "skills": skills
        }

