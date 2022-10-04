#get input of 2 to 6 characters
#while input contains any none alphanumeric or outside range, reprompt for input
#if numbers in middle of plate, reprompt
#if first number is a 0, reprompt #

def main(): #main function
    plate = input("Plate: ") #ask for plate
    if is_valid(plate): #execute is_valid function
        print("Valid") #if true, print valid
    else: #if not true
        print("Invalid") #print false


def is_valid(s): #define function is_valid
    if len(s) < 2 or len(s) > 6: #if the length is outside this range
        return False #return false
    elif s[0:2].isalpha() == False: #if the first 2 characters are not alpha
        return False #return false
    elif s[0:].isalnum() == False: #if the characters are not alphanumeric
        return False #return false
    elif first_number_checker(s) == False:
        return False
    elif number_in_middle(s) == False:
        return False
    else:
        return True


def first_number_checker(str): #define first_number_checker
    for l in str: #for each letter in string input
        if l == '0': #if l = '0'
            return False #indicates failed check
        elif l.isdigit(): #if l is digit
             if l != '0': #if number is not 0
                break #end before checking a second number

def number_in_middle(str): #define number_in_middle
    for c in str: #for each character in string
        if c.isdigit(): #if a character is digit
            str2 = str.split(c) #split the string
            for a in str2[1]: #for each character in the second half of the split
                if a.isalpha(): #if any character is alpha
                    return False #return false

main()