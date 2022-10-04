#import sys
#take one CLA (name/path of a python file)
#if not one CLA, sys.exit
#count lines of code, not including # or blank lines
    #read file
    #if starts with #
    #if blank
#output number of lines

import sys #needed to import CLA

def main():
    #execute code if sys len  == 2
    if len(sys.argv) == 2:
        try:
            if sys.argv[1].endswith(".py"):
                lines = count_lines(sys.argv[1])
                print(lines)
            else:
                sys.exit("Not a python file.")
        except FileNotFoundError: #cannot find file
            sys.exit("File does not exist.")

    #do this if len < 2
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    #do this if len > 2
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

def count_lines(CLA):
    counter = 0
    with open (CLA) as file:
        for line in file:
            if line.strip().startswith("#") or len(line.strip()) == 0:
                counter += 0
            else:
                counter += 1
        return(counter)

if __name__ == "__main__":
    main()