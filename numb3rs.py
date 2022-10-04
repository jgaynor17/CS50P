#import releveant libs
#get input
#put input through func
    #seperate each ip at "." through "\." - use raw string to accomodate for "\"
    #capture and check each number's range between 0 and 255

import re #import re.search
import sys
#cannot import any more libs


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.fullmatch(r"([\d]+)+\.+([\d]+)+\.+([\d]+)+\.+([\d]+)", ip): #fully match the format to be #.#.#.# - fullmatch means we dont need ^$, "([\d]+)" captures a digit with 1 or more repetitions, "+\." adds a "." to the search
        a = int(matches.group(1)) #assign variables to the matches
        b = int(matches.group(2))
        c = int(matches.group(3))
        d = int(matches.group(4))
        numbers = [a, b, c, d] #number list
        count = 0
        for number in numbers:
            if 0 <= number <= 255: #check each number is between 0 and 255
                count += 1 #can score max of 4
        if count == 4: #if all are within range
            return(True)
        else: #if not all within range
            return(False)
    else:
        return(False)


if __name__ == "__main__":
    main()