#while true
#try
#ask for input
#store input  to a dictionary and count the number of items, e.g., if banana entered twice, count 2 bananas
#except EOF error
#return grocery list alphabetically sorted

groceries = {} #defines groceries dictionary

while True:
    try:
        item = input().upper() #get input and capitalise
        if item in groceries.keys(): #if the item is in the dictionary
            groceries[item] += 1 #increase count by 1
        else:
            groceries[item] = 1 #set count to 1
            pass

    #error handling
    except KeyError:
        pass
    except RuntimeError:
        pass
    except EOFError:
        sorted_groceries = dict(sorted(groceries.items()))
        break

for item in sorted_groceries: #for each key in groceries
    print(groceries[item], item) #print the quantity and the key