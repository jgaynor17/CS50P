from bank import value

def test_value_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("Hello!") == 0

def test_value_hi():
    assert value("hi") == 20
    assert value("hey") == 20

def test_value_welcome():
    assert value("What's up") == 100
    assert value("WELCOME!") == 100