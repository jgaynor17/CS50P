#while true
    #prompt for items (case insensitive)
    #ignore non item input
    #add item price to total
    #print total price to 2dp
    #if they press control d then end input
#print final total

total = 0
menu = {
    "Baja Taco" : 4.00,
    "Burrito" : 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

while True:
    try:
        item = input("Item: ").title()
        for foods in menu:
            if item == foods:
                total += menu[foods]
                print("${0:.2f}".format(total))
                pass
            else:
                pass
    except EOFError:
        break

print("Total: " + "${0:.2f}".format(total))