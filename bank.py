greeting = input("What is your greeting? ") #get greeting
greeting = greeting.casefold().strip() #split the greeting into a list

if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")