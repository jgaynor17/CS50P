#get AD year input from user in middle-endian format
#assume all months have 31 days, invalidate any input with more than 31
#move input[2] to input[0]
#output to format YYYY:MM:DD

months = [
    {"name" : "January", "number" : "01", "no" : "1"},
    {"name" : "February", "number" : "02", "no" : "2"},
    {"name" : "March", "number" : "03", "no" : "3"},
    {"name" : "April", "number" : "04", "no" : "4"},
    {"name" : "May", "number" : "05", "no" : "5"},
    {"name" : "June", "number" : "06", "no" : "6"},
    {"name" : "July", "number" : "07", "no" : "7"},
    {"name" : "August", "number" : "08", "no" : "8"},
    {"name" : "September", "number" : "09", "no" : "9"},
    {"name" : "October", "number" : "10", "no" : "10"},
    {"name" : "November", "number" : "11", "no" : "11"},
    {"name" : "December", "number" : "12", "no" : "12"}
] #dict of months

punc = ",./;:-" #define variable of punctuation the user may input

#validate input
while True:
    try:
        middle_endian = str(input("Please enter an AD date formatted month, day, year ")).title()#get middleendian input and titlecase and split if there are spaces
        for c in middle_endian: #for character in input
            if c in punc: #if in punctuation variable
                middle_endian = middle_endian.replace(c, " ") #replace it with a space
        middle_endian = middle_endian.split() #split and convert to list

        month = (middle_endian[0]) #keep month as string in case of January or 01
        day = int(middle_endian[1]) #convert input to int
        year = int(middle_endian[2]) #convert input to int

        if (0 < day < 31) and (year > 0):
            for mon in months: #iterate through months dict
                if month == mon["name"] or month == mon["number"] or month == mon["no"]: #if month input = any assigned value of a month
                    month = mon["number"] #month now equals the number of that month
                    print(f"{year:04}-{month}-{day:02}".format()) #print the year, then month, then date and format the year and date
                    quit()
                else:
                    pass


    except IndexError: #unless there is an index error
        pass