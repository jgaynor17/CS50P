life = input("What is the answer to the great question of life, the universe, and everything? ")
life = life.strip().casefold()

if life == '42':
    print("Yes")
elif life == 'forty two':
    print("Yes")
elif life == ("forty-two"):
    print("Yes")
else:
    print ("No")