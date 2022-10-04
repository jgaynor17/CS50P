#get input
#scan for uppercase text
#if uppercase is found, convert to lower and insert _before it
#print camelCase

camelcase = input("camelCase: ") #get input

for c in camelcase: #for each character in camelcase variable
    if c.isupper(): #if the character is uppercase
        camelcase = camelcase.replace(c, "_" + c.lower()) #camelcase now equals camelcase but with capitals replaced by _ and lowercase
    snakecase = camelcase #define this altered input as snakecase

print(f"snake_case: {snakecase} ") #print snakecase