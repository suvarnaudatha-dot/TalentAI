
import re


def clean_jd_text(text: str) -> str:
    # Replace multiple spaces with a single space
    text = re.sub(r"[ \t]+", " ", text)

    # Remove spaces at the beginning and end of each line
    lines = [line.strip() for line in text.splitlines()]

    # Remove empty lines
    lines = [line for line in lines if line]

    # Join cleaned lines
    cleaned_text = "\n".join(lines)

    return cleaned_text.strip()

