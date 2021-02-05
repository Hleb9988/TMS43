import pytest

from tasks.lesson03.task311 import is_gmail


@pytest.mark.unit
def test():
    result = is_gmail("njhbjhbhbjh@gmail.com")
    assert "gmail.com" in result
