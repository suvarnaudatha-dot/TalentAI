
import re


def extract_sections(text: str) -> dict:
    sections = {
        "professional_summary": "",
        "technical_skills": "",
        "education": "",
        "projects": "",
        "certifications": "",
        "achievements": ""
    }

    section_patterns = {
        "professional_summary": r"PROFESSIONAL SUMMARY",
        "technical_skills": r"TECHNICAL SKILLS",
        "education": r"EDUCATION",
        "projects": r"PROJECTS",
        "certifications": r"CERTIFICATIONS",
        "achievements": r"COMPETITIVE PROGRAMMING & ACHIEVEMENTS"
    }

    positions = []

    for section_name, pattern in section_patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            positions.append(
                (match.start(), section_name, match.end())
            )

    positions.sort()

    for i, (start, section_name, end) in enumerate(positions):

        if i + 1 < len(positions):
            next_start = positions[i + 1][0]
            section_text = text[end:next_start]
        else:
            section_text = text[end:]

        sections[section_name] = section_text.strip()

    return sections
