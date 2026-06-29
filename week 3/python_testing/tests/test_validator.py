import pytest
from src.validator import valdiate_registration_password


def test_valdiate_registration_password():
    assert valdiate_registration_password("PyTest@2026") is True


def test_valid_minimum_length():
    assert valdiate_registration_password("aB1!dfjh") is True


def test_error_empty_string():
    with pytest.raises(ValueError, match="Password cannot be empty"):
        valdiate_registration_password("")


def test_error_too_short():
    with pytest.raises(
        ValueError, match="Password must be between 8 and 20 characters"
    ):
        valdiate_registration_password("Short1!")


def test_valid_maximum_length():
    assert valdiate_registration_password("aB1!dfjhfi2385839f") is True


def test_error_too_long():
    with pytest.raises(
        ValueError, match="Password must be between 8 and 20 characters"
    ):
        valdiate_registration_password("idsjoidjfpikdpskfpdkfspdofkpsokdpfk")


def test_password_contains_alnum():

    assert valdiate_registration_password("Pass@1234") is True


def test_error_password_contains_alnum():
    with pytest.raises(ValueError, match="Password must contain at least one digit"):
        valdiate_registration_password("HelloWorld")


def test_error_missing_uppercase():
    with pytest.raises(
        ValueError, match="Password must contain at least one uppercase letter"
    ):
        valdiate_registration_password("secure@123")


def test_error_missing_lowercase():
    with pytest.raises(
        ValueError, match="Password must contain at least one lowercase letter"
    ):
        valdiate_registration_password("SECURE@123")
