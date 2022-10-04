class Jar:
    def __init__(self, capacity=12): #initialise a cookie jar with capacity being 12
        self.capacity = capacity #Attribute of the self, i.e., attribute of jar
        self.size = 0 #Attribute of the self, i.e., attribute of jar

    def __str__(self):
        return "🍪" * self.size #multiply the size (number of cookies in the jar) by the string to return x cookies

    def deposit(self, n):
        self.size += n #increasse size by n

    def withdraw(self, n):
        self.size -= n #decrease size by n

    @property #GETTER - max no of cookies that can be in the jar
    def capacity(self):
        return (self._capacity) #as variable and property share a name, the variable is given a _ at the front of the name avoiding it running through the setter on a loop.

    @capacity.setter #SETTER, runs whenever .capacity is called
    def capacity (self, capacity):
        if capacity < 0:
            raise ValueError ("Invalid capacity") #invalidate a cookie jar with non positive int capacity
        self._capacity = capacity

    @property #GETTER
    def size(self):
        return (self._size) #as variable and property share a name, the variable is given a _ at the front of the name avoiding it running through the setter on a loop.

    @size.setter #SETTER, runs whenever .size is called
    def size(self, size):
        if size < 0: #if size is negative
            raise ValueError("There aren't enough cookies!")
        if size > self.capacity: #if size exceeds jar capacity
            raise ValueError("There isn't enough space!")
        self._size = size #attribute is equal to the variable size

def main():
    capacity = int(input("Capacity: ")) #Get capacity
    deposit = int(input("Deposit: ")) #get deposit
    withdraw = int(input("Withdraw: ")) #get withdraw
    cookies = Jar(capacity) #assign capacity
    cookies.deposit(deposit) #add the deposit
    cookies.withdraw(withdraw) #subtract withdraw
    print(cookies.capacity) #return
    print(cookies.size) #return


if __name__ == "__main__":
    main()