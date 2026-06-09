class BankAccount: # It is a class
    def __init__(self, owner, acc, balance): #  Constructor ek special function hai jo object bante hi automatically chal jata hai.
        self.owner = owner
        self.acc = acc
        self.__balance = balance 
    
    def deposite(self, amount):
        if amount <= 0:
            print("Invalid amount")
        else:   
            self.__balance += amount
            print(f"The amount {amount} is deposited")

    def check_balance(self):
        print(f"The current balance of your account is: {self.__balance}")
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print("You have insufficient balance in your account")
        else:
            self.__balance -= amount
            print(f"The amount {amount} is deducted")

b1 = BankAccount("Bhushan", 13476846, 0) # It is an object which holds the real data representing the class 


# print(b1.balance) #This will not work because the name is mangled here
# print(b1._BankAccount__balance) # This will work because it can directly access the variable
# b1.deposite(50000)
# b1.check_balance()
# b1.withdraw(250000)
# b1.check_balance()