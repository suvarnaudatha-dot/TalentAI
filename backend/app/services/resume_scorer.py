
def calculate_resume_score(sections: dict, skills: list) -> dict:

    score = 0

    # Professional Summary - 15 points
    if sections.get("professional_summary"):
        score += 15

    # Technical Skills - 20 points
    if sections.get("technical_skills"):
        score += 20

    # Education - 15 points
    if sections.get("education"):
        score += 15

    # Projects - 20 points
    if sections.get("projects"):
        score += 20

    # Certifications - 10 points
    if sections.get("certifications"):
        score += 10

    # Achievements - 10 points
    if sections.get("achievements"):
        score += 10

    # Resume completeness - 10 points
    if len(skills) >= 10:
        score += 10
    elif len(skills) >= 5:
        score += 5

    # Generate feedback
    feedback = []

    if not sections.get("professional_summary"):
        feedback.append("Add a professional summary.")

    if not sections.get("technical_skills"):
        feedback.append("Add a technical skills section.")

    if not sections.get("education"):
        feedback.append("Add education details.")

    if not sections.get("projects"):
        feedback.append("Add relevant projects.")

    if not sections.get("certifications"):
        feedback.append("Add relevant certifications.")

    if not sections.get("achievements"):
        feedback.append("Add achievements or competitive programming experience.")

    if len(skills) < 10:
        feedback.append("Add more relevant technical skills.")

    return {
        "score": score,
        "max_score": 100,
        "feedback": feedback
    }

