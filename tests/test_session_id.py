from what_is_entire import generate_session_id


def test_generate_session_id_default_length():
    """Test that default session ID has correct length."""
    session_id = generate_session_id()
    assert len(session_id) == 16
    assert all(c in "0123456789abcdef" for c in session_id)


def test_generate_session_id_custom_length():
    """Test that custom length works correctly."""
    session_id = generate_session_id(length=4)
    assert len(session_id) == 8
    assert all(c in "0123456789abcdef" for c in session_id)


def test_generate_session_id_uniqueness():
    """Test that multiple calls generate different IDs."""
    ids = {generate_session_id() for _ in range(100)}
    assert len(ids) == 100  # All should be unique
