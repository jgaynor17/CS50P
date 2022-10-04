def main():
    dollars = dollars_to_float(input("How much was the meal? ")) #get and run input through dollarstofloat
    percent = percent_to_float(input("What percentage would you like to tip? ")) #get and run input through percenttofloat
    tip = dollars * percent #multiply dollars and percent after being ran through functions
    print(f"Leave ${tip:.2f}") #print how much to leave to 2dp?


def dollars_to_float(d): #dtf function, d = dollars
    d = d.removeprefix("$") #removes dollar prefix from new variable newdollar
    nd = float(d) #converts string without $ to a float
    return(nd) #returns the value to the variable d


def percent_to_float(p): #ptf function, p = percent
    p = p.removesuffix("%") #removes % suffix from new variable newpercent
    np = float(p) / 100 #converts string to float after remvoing % then divides by 100
    return(np) #returns the value to the variable p

main()