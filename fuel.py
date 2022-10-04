def main(): #main loops input for fraction whilst invalid type is entered
        frac = input("Please enter a fraction: ")
        deci = convert(frac)
        percent = gauge(deci)
        print(percent)



def convert(frac):
    while True:
        try:
            numerator, denominator = frac.split("/")
            new_numerator = int(numerator)
            new_denominator = int(denominator)
            f = new_numerator / new_denominator
            if f <= 1:
                d = int(f * 100)
                return d
            else:
                frac = input("Please enter a fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise



def gauge(decimal):
    if decimal <= 1:
        return("E")
    elif decimal >= 99:
        return("F")
    else:
        return(f"{decimal}%")



if __name__ == "__main__":
    main()