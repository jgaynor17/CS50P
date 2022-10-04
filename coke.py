#make variable coke = 50
#get input of money put into machine (coin), if invalid coin, reprompt
#coke - coin
#loop while coke - coin > 0
#if coke - coin <= 0
#do change owed

coke = 50 #variable coke = 50

while coke > 0: #whilst coke > coin
    print("Amount due: " + f"{coke}") #print the amount due
    coin = int(input("Insert coin: ")) #get input for coin
    if coin == 5 or coin == 10 or coin == 25: #if the coin input matches one of these
        coke = coke - coin #subtract coin from coke
    else: #otherwise
        coke = coke #coke stays the same

if coke < 1: #when the amount has been paid, i.e., below 1 cent left to pay
    print(f"Change owed: {0 - coke}") #return change