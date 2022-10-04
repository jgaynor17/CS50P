from datetime import date
import inflect
import sys

p = inflect.engine()



def main():
    print(convert(input("Enter your date of birth: ")))

def convert(d):
    #VALIDATION CHECKING
    try:
        d = date.fromisoformat(d) #validate YYYY-MM-DD format
    except ValueError:
        sys.exit("Invalid date format, please use the format YYYY-MM-DD.")

    #IF VALID
    today = date.today() #variable created to allow subtraction of d from date.today
    if today >= d:
        difference = today - d
        minutes = int(difference.total_seconds() / 60) #int removes decimal
        mins = p.number_to_words(minutes)  #convert to words
        mins = mins.replace("and ", "")
        return(f"{mins} minutes".capitalize())
    else:
        sys.exit("Invalid date.")


if __name__ == "__main__":
    main()

