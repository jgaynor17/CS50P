#import re and sys (both optional but no additional libs)
#get input of time in 12 hr format #:## AM to #:## PM or # AM to # PM
#raise ValueError if input doesn't match the above format or if time is invalid

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.fullmatch(r"([1-9][0-9]?) (AM|PM) to ([1-9][0-9]?) (AM|PM)", s): #if matches # AM/PM to # AM/PM format:
        s_hr = int(matches.group(1)) #hr variable = first group match
        e_hr = int(matches.group(3)) #hr variable = third group match
        if s_hr > 12 or s_hr < 1 or e_hr > 12 or e_hr < 1:
            raise(ValueError)
        if matches.group(2) == "AM": #if AM
            if s_hr != 12:
                start = (f"{s_hr:02}:00") #start variable formats hr
            else:
                start = (f"{s_hr-12:02}:00") #12 AM becomes 00
        else: #if PM
            if s_hr != 12:
                start = (f"{s_hr+12:02}:00") #start variable formats hr
            else:
                start = (f"{s_hr:02}:00") #start variable formats hr
        if matches.group(4) == "AM": #if AM
            if e_hr != 12:
                end = (f"{e_hr:02}:00") #start variable formats hr
            else:
                end = (f"{e_hr-12:02}:00") #12 AM becomes 00
        else: #if PM
            if e_hr != 12:
                end = (f"{e_hr+12:02}:00") #start variable formats hr
            else:
                end = (f"{e_hr:02}:00") #start variable formats hr

        return(f"{start} to {end}")

    elif matches := re.search(r"^([1-9][0-9]?:\d\d) (AM|PM) to ([1-9][0-9]?:\d\d) (AM|PM)", s): #elif matches #:## AM/PM to #:## AM/PM format:
        s_hr, s_min = matches.group(1).split(":") #split into hours and mins
        s_hr = int(s_hr) #convert to int
        s_min = int(s_min) #convert to int
        e_hr, e_min = matches.group(3).split(":") #split into hours and mins
        e_hr = int(e_hr) #convert to int
        e_min = int(e_min) #convert to int
        if s_hr > 12 or s_hr < 1 or e_hr > 12 or e_hr < 1 or s_min > 59 or e_min > 59:
            raise(ValueError)

        if matches.group(2) == "AM": #if AM
            if s_hr != 12:
                start = (f"{s_hr:02}:{s_min:02}") #start variable formats hr
            else:
                start = (f"{s_hr-12:02}:{s_min:02}") #12 AM becomes 00
        else: #if PM
            if s_hr != 12:
                start = (f"{s_hr+12:02}:{s_min:02}") #start variable formats hr
            elif s_hr == 12:
                start = (f"{s_hr-12:02}:{s_min:02}") #start variable formats hr
        if matches.group(4) == "AM": #if AM
            if e_hr != 12:
                end = (f"{e_hr:02}:{e_min:02}") #end variable formats hr and min
            else:
                end = (f"{e_hr-12:02}:{e_min:02}") #end variable formats hr and min
        else: #if PM
            if e_hr != 12:
                end = (f"{e_hr+12:02}:{e_min:02}") #end variable formats hr and min
            else:
                end = (f"{e_hr:02}:{e_min:02}") #end variable formats hr and min

        return(f"{start} to {end}")

    else:
        raise(ValueError)


if __name__ == "__main__":
    main()


#9:30 AM to 5:30 PM
#9 AM to 5 PM