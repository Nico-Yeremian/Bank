class Bank:
    def __init__(self, name):
        self.username = name
        self.balance = 100
        self.allAccounts = []

    def addAccount(self, username, password):
        self.username = username
        self.password = password

    class Account:
        def __init__(self, username, password):
            self.username = username
            self.password = password


    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

ChaseBank = Bank("Chase Bank")

input()
ChaseBank.deposit(int(input("How much would you like to deposit? ")))
ChaseBank.withdraw(int(input("How much would you like to withdraw? ")))
