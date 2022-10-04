from plates import is_valid

def test_is_valid_all_alpha():
    assert is_valid("AAAAAA") == True
    assert is_valid("aaaaaa") == True

def test_is_valid_all_num():
    assert is_valid("123456") == False
    assert is_valid("123456") == False

def test_is_valid_alnum():
    assert is_valid("TEST12") == True
    assert is_valid("Te34st") == False
    assert is_valid("Test01") == False

def test_is_valid_punc():
    assert is_valid("Test3!") == False
    assert is_valid("!!!!!") == False

def test_is_valid_length():
    assert is_valid("IMSOLONG11!") == False
    assert is_valid("A") == False
    assert is_valid("") == False