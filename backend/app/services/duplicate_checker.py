import hashlib


def generate_text_hash(text: str) -> str:
    """
    Generate a unique SHA-256 hash for resume text.
    """

    normalized_text = " ".join(text.lower().split())

    return hashlib.sha256(
        normalized_text.encode("utf-8")
    ).hexdigest()


def is_duplicate(
    new_text: str,
    existing_hashes: list[str]
) -> bool:
    """
    Check whether the resume already exists.
    """

    new_hash = generate_text_hash(new_text)

    return new_hash in existing_hashes