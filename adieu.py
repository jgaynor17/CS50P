#get names and reprompt
#loop until control d
#print aideu, adieu to all names, separating all by , except the final which should be separated by "and"

import inflect #import the module
p = inflect.engine() #assign p to the funcs from inflect

names = [] #blank list of names

while True: #forever
    try: #try this
        names.append(input("Name: ")) #append names to the list

    except EOFError: #except ctrl D
        goodbye = p.join(names[0:]) #variable goodbye = concotonation of names seperated by "," until n-1 which is separated by "and"
        print(f"Adieu, adieu, to {goodbye}") #print adieu to list of names
        break #end the loop