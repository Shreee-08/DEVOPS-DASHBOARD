from main import add

def test_add_basic():
    assert add(2, 3) == 5

def test_add_zero():
    assert add(0, 0) == 0
