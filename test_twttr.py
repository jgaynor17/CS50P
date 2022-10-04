#import twitter file from week 2
#get function that removes vowels
#allow user to input word to remove vowels from
#return output only (__name__ == "__main__")

from twttr import shorten

def test_shorten_word_mix_case():
    assert shorten("HEllo")=="Hll"

def test_shorten_num():
    assert shorten("12345")=="12345"

def test_shorten_alnum():
    assert shorten("Hello 30 people")=="Hll 30 ppl"

def test_shorten_punc():
    assert shorten("Let's see what's next...")=="Lt's s wht's nxt..."