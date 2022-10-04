from working import convert
import pytest

def main():
    test_hour_only()
    test_hours_minutes()
    test_PM_to_AM_hours()
    test_PM_to_AM_hours_minutes()
    test_invalid_minute()
    test_hyphen()
    test_invalid_hour()
    test_invalid_format()

def test_hour_only():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_hours_minutes():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:30 AM to 9:30 PM") == "09:30 to 21:30"

def test_PM_to_AM_hours():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

def test_PM_to_AM_hours_minutes():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_invalid_minute():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_hyphen():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_invalid_hour():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")

def test_invalid_format():
    with pytest.raises(ValueError):
        #convert("cat")
        #convert("2;00 AM to 4!30 PM")
        #convert("17:00 AM to 9:00 PM")
        #convert("1: AM to 9: PM")
        #convert("0 to 9")
        #convert("03 AM to 01 PM")
        #convert("09:00 am - 17:00 PM")
        convert("00:00 AM - 7:00 PM")

if __name__ == "__main__":
    main()