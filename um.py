#import re and sys
#run input through count function
#count - re.findall - finds all counts of um
#for number of ums, increase count variable by 1
#return count

import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    ums = [] #list that all "ums" are added to
    if matches := re.findall(r"\bum\b",s.casefold()): #if there is a match of an "um" regardless of case or where it is in the sentence as long as it is a standalone word
        for i in matches: # for each of the matches
            ums.append(matches) #append to list "ums"
    return(len(ums)) #return the length of the list, i.e. the number of variables


if __name__ == "__main__":
    main()