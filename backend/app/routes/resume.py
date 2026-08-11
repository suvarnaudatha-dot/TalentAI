from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.pdf_parser import extract_text_from_pdf
from app.services.text_cleaner import clean_text
from app.services.section_extractor import extract_sections
from app.services.skill_extractor import extract_skills
from app.services.resume_scorer import calculate_resume_score
from app.services import storage

import os
import shutil
import tempfile


router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    allowed_types = [
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ]

    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are allowed."
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
            # Save uploaded PDF temporarily
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

            # Step 3: Extract sections
            sections = extract_sections(
                cleaned_text
            )

            # Step 4: Extract skills
            skills = extract_skills(
                cleaned_text
            )

            # Step 5: Calculate resume score
            resume_score = calculate_resume_score(
                sections,
                skills
            )

            # Step 6: Check duplicate
            duplicate = storage.check_duplicate_resume(
                cleaned_text
            )

            # Step 7: Save to Supabase
            if not duplicate:

                resume_id = storage.save_resume(
                    filename=file.filename,
                    content_type=file.content_type,
                    extracted_text=cleaned_text,
                    resume_score=resume_score["score"],
                    duplicate=False,
                    skills=skills
                )

            else:
                resume_id = None

        finally:
            # Delete temporary file
            if os.path.exists(temp_file.name):
                os.unlink(temp_file.name)

        # Duplicate response
        if duplicate:
            return {
                "filename": file.filename,
                "content_type": file.content_type,
                "message": "Duplicate resume detected",
                "duplicate": True
            }

        # Successful PDF response
        return {
            "filename": file.filename,
            "content_type": file.content_type,
            "message": "Resume analysis completed and saved successfully",
            "duplicate": False,
            "resume_id": resume_id,
            "extracted_text": cleaned_text,
            "sections": sections,
            "skills": skills,
            "resume_score": resume_score
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
            # Save uploaded DOCX temporarily
            shutil.copyfileobj(file.file, temp_file)
            temp_file.close()

            # Step 1: Read DOCX
            from docx import Document

            document = Document(
                temp_file.name
            )

            paragraphs = []

            for paragraph in document.paragraphs:

                if paragraph.text.strip():

                    paragraphs.append(
                        paragraph.text.strip()
                    )

            extracted_text = "\n".join(
                paragraphs
            )

            # Step 2: Clean text
            cleaned_text = clean_text(
                extracted_text
            )

            # Step 3: Extract sections
            sections = extract_sections(
                cleaned_text
            )

            # Step 4: Extract skills
            skills = extract_skills(
                cleaned_text
            )

            # Step 5: Calculate resume score
            resume_score = calculate_resume_score(
                sections,
                skills
            )

            # Step 6: Check duplicate
            duplicate = storage.check_duplicate_resume(
                cleaned_text
            )

            # Step 7: Save to Supabase
            if not duplicate:

                resume_id = storage.save_resume(
                    filename=file.filename,
                    content_type=file.content_type,
                    extracted_text=cleaned_text,
                    resume_score=resume_score["score"],
                    duplicate=False,
                    skills=skills
                )

            else:
                resume_id = None

        finally:
            # Delete temporary file
            if os.path.exists(temp_file.name):
                os.unlink(temp_file.name)

        # Duplicate response
        if duplicate:
            return {
                "filename": file.filename,
                "content_type": file.content_type,
                "message": "Duplicate resume detected",
                "duplicate": True
            }

        # Successful DOCX response
        return {
            "filename": file.filename,
            "content_type": file.content_type,
            "message": "Resume analysis completed and saved successfully",
            "duplicate": False,
            "resume_id": resume_id,
            "extracted_text": cleaned_text,
            "sections": sections,
            "skills": skills,
            "resume_score": resume_score
        }