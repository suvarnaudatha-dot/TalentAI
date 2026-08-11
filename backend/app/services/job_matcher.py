import re


KEYWORDS = [
    "python",
    "java",
    "c++",
    "c",
    "sql",
    "javascript",
    "html",
    "css",
    "mongodb",
    "mysql",
    "dbms",
    "machine learning",
    "deep learning",
    "generative ai",
    "artificial intelligence",
    "tensorflow",
    "computer vision",
    "opencv",
    "mediapipe",
    "flutter",
    "dart",
    "firebase",
    "fastapi",
    "streamlit",
    "langchain",
    "pandas",
    "numpy",
    "matplotlib",
    "scikit-learn",
    "git",
    "github",
    "excel",
    "microsoft office",
    "quality assurance",
    "quality analyst",
    "defect analysis",
    "defect tracking",
    "data analysis",
    "data analytics",
    "analytical thinking",
    "critical thinking",
    "problem solving",
    "problem-solving",
    "communication",
    "verbal communication",
    "customer service",
    "time management",
    "teamwork",
    "team player",
    "organization",
    "organizational skills",
    "testing",
    "reporting",
    "investigation",
    "quality improvement",
    "data accuracy",
]


def extract_keywords(text: str) -> list[str]:
    """
    Extract relevant keywords from resume or job description.
    """

    text = text.lower()

    found_keywords = []

    for keyword in KEYWORDS:

        # Special handling for single-letter C
        if keyword == "c":
            pattern = r"(?<![a-z])c(?![a-z])"
        else:
            pattern = r"(?<![a-z0-9])" + re.escape(keyword) + r"(?![a-z0-9])"

        if re.search(pattern, text):
            found_keywords.append(keyword)

    return sorted(set(found_keywords))


def calculate_match(
    resume_text: str,
    job_description_text: str
) -> dict:
    """
    Compare resume with job description.
    """

    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(job_description_text)

    matched_skills = [
        keyword
        for keyword in jd_keywords
        if keyword in resume_keywords
    ]

    missing_skills = [
        keyword
        for keyword in jd_keywords
        if keyword not in resume_keywords
    ]

    if jd_keywords:
        match_score = round(
            (len(matched_skills) / len(jd_keywords)) * 100
        )
    else:
        match_score = 0

    if match_score >= 80:
        recommendation = "Excellent match"
    elif match_score >= 60:
        recommendation = "Good match"
    elif match_score >= 40:
        recommendation = "Moderate match"
    else:
        recommendation = "Low match"

    return {
        "match_score": match_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "resume_keywords": resume_keywords,
        "job_description_keywords": jd_keywords,
        "recommendation": recommendation
    }