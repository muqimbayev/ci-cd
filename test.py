import pytest
from python1 import fibonacci

def test_fibonacci():
    assert fibonacci(10) == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

test_fibonacci()