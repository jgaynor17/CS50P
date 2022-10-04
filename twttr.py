#get input
#whilst ignoring case, remove vowels
#return altered text

vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'] #list of vowels

def main():
    textspeak = input("Input: ") #get input
    print(shorten(textspeak))

def shorten(s):
    for c in s: #iterate through input
        if c in vowels[0:]: #if c == one of the vowels
            s = s.replace(c, "") #replace c with nothing
    return f"{s}"

if __name__ == "__main__":
    main()