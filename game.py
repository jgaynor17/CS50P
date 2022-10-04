#import random
#ask user to input a positive int = n
#randomly generate a number between 1 and n = r
#prompt user for a guess = g
#if g < r, print too small
#elif g > r, print too large
#else just right!


import random #imports the random module
g = -1 #assigned so that g can never = r from the beginning

while True: #forever loop
    try:
        n = int(input("Please enter a number within which you want to guess a random number: ")) #get int input
        if n < 1: #validates input > 1
            pass
        else:
            break
    except ValueError: #reprompts at value error
        pass

r = random.randint(1, n) #randomly generates between 0 and n

while g != r: #whilst the guess doesnt equal the random number
    try:
        g = int(input("Guess: "))
        if g > n or g < 1: #rejects any guess where g is greater than the level
            pass
        elif g > r:
            print("Too large!")
        elif g < r:
            print("Too small!")
        else:
            print("Just right!")
    except ValueError:
        pass