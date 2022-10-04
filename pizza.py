#import CSV and tabulate
#take csv file at CL
#reject input if not CSV, not sys len 2
#read csv file and separate values at comma

import sys
import csv
from tabulate import tabulate

pizzas = []

def main():
    try:
        if len(sys.argv) == 2:
            if sys.argv[1].endswith(".csv"):
                format(sys.argv[1])
                print(tabulate(pizzas, headers="keys", tablefmt="grid")) #pizzas is tabulated, the keys are the headers, the table format is "grid"
            else:
                sys.exit("Not a CSV file.")

        elif len(sys.argv) > 2:
            sys.exit("Too many arguments.")

        elif len(sys.argv) < 2:
            sys.exit("Too few arguments.")

    except FileNotFoundError:
        sys.exit("File not found.")

def format(CLA):
    with open (CLA) as file:
        DictReader = csv.DictReader(file)
        for row in DictReader:
            pizzas.append(row) #or more complicated pizzas.appendpizzas.append({"type" : row["Regular Pizza"], "small": row["Small"], "large": row["Large"]})

if __name__ == "__main__":
    main()