#get fraction input, X and Y must be ints and X must be <= Y
#divide numerator by denominator
#multiply by 100 and round to nearest int
#if below 1%, round to E

while True: #while true
    try: #attempt
        fraction = input("Enter a fraction: ") #get input fraction
        fraction = fraction.split(sep="/") #split the inputs into integers at /
        numerator = int(fraction[0]) #define numerator
        denominator = int(fraction[1]) #define denominator
        if numerator <= denominator:  #if n <= d
            break #break loop
        else: #else
            print("The numerator must be less than or equal to than the denominator.") #print that n must be <= d
            pass #pass
    except ValueError: #if there is a ValueError
        print("Please use the format X/Y.") #print to use the correct format
        pass #pass
    except ZeroDivisionError: #if there is a zero division error
        print("The denominator cannot be 0.") #print that the denominator cannot be 0
        pass #pass
    except IndexError:
        print("Please use the format X/Y.") #print to use the correct format
        pass #pass

percent = numerator / denominator * 100 #percent of fraction = the following
percent = round(percent) #round to nearest number
if percent >= 99: #if percent = 100
    print("F") #print F
elif percent <= 1: #if percent <= 1
    print("E") #print E
else: #else
    print(f'{percent}' + '%') #print the percent