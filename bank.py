#This file has been modified to award $100 for Hello and $0 for non H greetings

def main():
    greeting = input("What is your greeting? ").strip() #get greeting
    print(f"${value(greeting)}")

def value(greeting):
    greeting = greeting.lower()
    if greeting.startswith("hello"):
        return(0)
    elif greeting.startswith("h"):
        return(20)
    else:
        return(100)

if __name__ == "__main__":
    main()