# TalentAI

### Intelligent Recruitment & Resume Analysis Platform

TalentAI is a recruitment platform that automates **resume ingestion, text extraction, skill extraction, resume scoring, duplicate detection, and candidate data storage**.

## Features

* PDF & DOCX resume upload
* Resume text extraction and cleaning
* Resume section extraction
* Automatic skill extraction
* Resume scoring
* Duplicate resume detection
* Supabase PostgreSQL storage
* FastAPI REST APIs
* React.js frontend

## Tech Stack

* **Backend:** Python, FastAPI, Uvicorn
* **Processing:** PyPDF, python-docx
* **Frontend:** React.js, Vite
* **Database:** Supabase PostgreSQL
* **Tools:** Git, GitHub, Swagger

## Architecture

```text
Resume Upload
     ↓
Text Extraction
     ↓
Text Cleaning
     ↓
Section & Skill Extraction
     ↓
Resume Scoring
     ↓
Duplicate Detection
     ↓
Supabase PostgreSQL
```

## API

**Health Check**

```http
GET /
```

**Resume Upload**

```http
POST /resume/upload
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

## Project Status

**Week 1 — Resume Ingestion & Data Pipeline ✅**

* Resume ingestion
* Text processing
* Skill extraction
* Resume scoring
* Duplicate detection
* Database persistence

## Developer

**Udatha Suvarna**
B.Tech — Artificial Intelligence & Machine Learning

## License

Developed for educational and internship purposes.

