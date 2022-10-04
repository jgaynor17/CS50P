def main():
    equation = input("Please enter a mathematical equation in the format x [+, -, *, /] y: ").strip().split()
    first_no = float(equation[0])
    second_no = float(equation[2])

    if equation[1] == '+':
        addition(first_no, second_no)
    elif equation[1] == '-':
        subtraction(first_no, second_no)
    elif equation[1] == '*':
        multiplication(first_no, second_no)
    elif equation[1] == '/':
        division(first_no, second_no)
    else:
        print("Invalid equation.")

def addition(x, y):
    z = x + y
    print(z)

def subtraction(x, y):
    z = x - y
    print(z)

def multiplication(x, y):
    z = x * y
    print(z)

def division(x, y):
    z = x / y
    print(z)

main()