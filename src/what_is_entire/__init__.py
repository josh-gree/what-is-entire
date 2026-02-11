import secrets


def hello() -> str:
    return "Hello from what-is-entire!"


def generate_session_id(length: int = 8) -> str:
    """Generate a random hexadecimal session ID.

    Args:
        length: Number of bytes to generate (default 8, produces 16 hex chars)

    Returns:
        A hexadecimal string of length * 2 characters

    Example:
        >>> session_id = generate_session_id()
        >>> len(session_id)
        16
        >>> all(c in '0123456789abcdef' for c in session_id)
        True
    """
    return secrets.token_hex(length)
