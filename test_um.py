from Week_7.um import count
import pytest

def main():
    test_um()
    test_um_punc()
    test_um_punc_sentence()
    test_words_sep_commas()
    test_sentence()

def test_um():
    assert count("um") == 1

def test_um_punc():
    assert count("um, um!") == 2

def test_um_punc_sentence():
    assert count("Um, thanks for the album.") == 1

def test_words_sep_commas():
    assert count("Um, thanks, um...") == 2

def test_sentence():
    assert count("Hello there everyone!") == 0

if __name__ == "__main__":
    main()