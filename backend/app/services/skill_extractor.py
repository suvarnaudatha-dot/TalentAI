
import re


# Common technical and professional skills
SKILL_LIST = [
    # Programming Languages
    "python",
    "java",
    "javascript",
    "typescript",
    "c++",
    "c",
    "c#",
    "sql",

    # Databases
    "mysql",
    "mongodb",
    "postgresql",
    "sqlite",
    "database",
    "dbms",

    # Data / Analytics
    "data analytics",
    "data analysis",
    "data visualization",
    "statistics",
    "reporting",
    "excel",
    "microsoft excel",
    "power bi",
    "tableau",

    # AI / ML
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "generative ai",
    "tensorflow",
    "pytorch",
    "scikit-learn",
    "computer vision",
    "nlp",
    "opencv",
    "mediapipe",

    # Web / Backend
    "html",
    "css",
    "react",
    "node.js",
    "fastapi",
    "flask",
    "streamlit",
    "rest api",

    # Cloud / Tools
    "aws",
    "azure",
    "gcp",
    "git",
    "github",
    "docker",

    # Frameworks / Libraries
    "pandas",
    "numpy",
    "matplotlib",
    "langchain",
    "flutter",
    "dart",
    "firebase",

    # Core CS
    "data structures",
    "algorithms",
    "object oriented programming",
    "oops",

    # Soft Skills
    "problem solving",
    "problem-solving",
    "communication",
    "written communication",
    "verbal communication",
    "teamwork",
    "team player",
    "leadership",
    "critical thinking",
    "analytical thinking",
    "time management",
    "organization",
    "organizational skills",
    "customer service",

    # Job-specific terms
    "quality analyst",
    "quality assurance",
    "quality analysis",
    "defect analysis",
    "defect tracking",
    "quality improvement",
    "data accuracy",
    "investigation",
    "microsoft office",
]


def extract_skills(text: str) -> list[str]:
    """
    Extract known skills and keywords from resume/JD text.
    """

    if not text:
        return []

    text_lower = text.lower()

    found_skills = []

    for skill in SKILL_LIST:

        # Escape special characters such as +, #, .
        escaped_skill = re.escape(skill)

        # Match complete words/phrases
        pattern = rf"(?<!\w){escaped_skill}(?!\w)"

        if re.search(pattern, text_lower):
            # Keep original skill formatting
            if skill not in found_skills:
                found_skills.append(skill)

    return found_skills

