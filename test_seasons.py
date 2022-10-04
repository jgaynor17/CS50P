from Week_8.seasons.seasons import convert
import pytest

def main():
    test_invalid_format()
    test_year_ago()
    test_2_years_ago()
    test_future()
    test_DD_MM()

def test_invalid_format():
    with pytest.raises(SystemExit):
        convert("January 1, 1999")

def test_year_ago():
    assert convert("2021-09-28") == "Five hundred twenty-five thousand, six hundred minutes"

def test_2_years_ago():
    assert convert("2020-09-28") == "One million, fifty-one thousand, two hundred minutes"

def test_future():
    with pytest.raises(SystemExit):
        convert("2029-10-24")

def test_DD_MM():
    with pytest.raises(SystemExit):
        convert("2000-24-10")


if __name__ == "__main__":
    main()