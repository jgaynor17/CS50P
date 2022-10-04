filename = input("Please enter a file name and attach a type, e.g., 'hello.jpg': ") #take input
filename = filename.casefold().strip().split('.') #desensitise to case, strip, and split so the ending can be isolated

if len(filename) == 1: #if length is equal to 1, i.e., no extension
    print("application/octet-stream") #error default
elif filename[-1] == 'gif' or filename[-1] == 'jpeg' or filename[-1] == 'png': #if any of these endings
    print("image/" + f"{filename[-1]}") #print image + filetype
elif filename[1] == 'jpg': #if the file extension is 'jpg'
        print("image/jpeg")#print text
elif filename[-1] == 'pdf' or filename[-1] == 'zip': # if any of these endings
    print("application/"  + f"{filename[-1]}") #print application + filetype
elif filename[-1] == 'txt': #if this ending
    print("text/plain")#print text
else: #in any other case
    print("application/octet-stream") #error default
