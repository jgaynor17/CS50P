def main():
    time = input("What is the time (24hour clock)? ").strip().split(':')
    if int(time[1]) > 59:
        return
    else:
        convert(time)

def convert(clock):
    hours = int(clock[0])
    minutes = int(clock[1])

    if hours == 7 or hours == 8 and minutes == 0:
        print("Breakfast time")

    elif hours == 12 or hours == 13 and minutes == 0:
        print("Lunch time")

    elif hours == 18 or hours == 19 and minutes == 0:
        print("Dinner time")
    else:
        return

main()
