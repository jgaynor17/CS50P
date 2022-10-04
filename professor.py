#prompt user for int input for level, this can be 1, 2 or 3, reprompt if not in this range
#randomly produce 10 maths problems formatted X + Y, only addition
#if answer is correct move to next question, else print EEE and prompt again up to 3 times before displaying correct answer before moving on.
#after 10 qs give score out of 10

import random



def main():
    q = 0
    t = 0
    score = 0
    level = get_level()

    while q < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        while t < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                t += 1
                if answer == x + y:
                    q += 1
                    t = 0
                    score += 1
                    break
                else:
                    print("EEE")
                    if t < 3:
                        pass
                    elif t == 3:
                        print(f"{x} + {y} = {x + y}")
                        q += 1
                        t = 0
                        break
            except ValueError:
                pass

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Please enter a level (1, 2 or 3): "))
            if level <1 or level >3:
                pass
            else:
                return level
        except ValueError:
            pass



def generate_integer(level):
    try:
        if level == 1:
            n = random.randint(0,9)
            return(n)

        elif level == 2:
            n = random.randint(10,99)
            return(n)

        elif level == 3:
            n = random.randint(100,999)
            return(n)

    except ValueError:
        pass



if __name__ == "__main__":
    main()