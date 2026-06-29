import re


def valdiate_registration_password(password: str) -> bool:
    if not password:
        raise ValueError("Password cannot be empty")

    if not (8 <= len(password) <= 20):
        raise ValueError("Password must be between 8 and 20 characters")

    if not re.search(r"[a-z]", password):
        raise ValueError("Password must contain at least one lowercase letter")

    if not re.search(r"[A-Z]", password):
        raise ValueError("Password must contain at least one uppercase letter")

    if not re.search(r"[0-9]", password):
        raise ValueError("Password must contain at least one digit")

    if not re.search(r"[@#\$%!\*&]", password):
        raise ValueError("Password must contain at least one special character")

    return True
