import pytest


@pytest.fixture()
def setup():
    print("This is Setup Method")
    yield
    print("This is yield")


def test_login(setup):
    print("In login method")


def test_sign_up(setup):
    print("In sign up method")
