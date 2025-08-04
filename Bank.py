class Bank:
    def __init__(self, name):
        self.username = name
        self.balance = 100

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

ChaseBank = Bank("Chase Bank")
ChaseBank.deposit(int(input("How much would you like to deposit? ")))
ChaseBank.withdraw(int(input("How much would you like to withdraw? ")))
