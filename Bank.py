class Bank:
    def __init__(self, name):
        self.username = name
        self.balance = 100000
        self.allAccounts = []

    class Account:
        def __init__(self, username, password, balance, number):
            self.username = username
            self.password = password
            self.balance = balance
            self.number = number.randint(1, 999999)

    def add_account(self, username, password, balance):
        new_account = self.Account(username, password, balance)
        self.allAccounts.append(new_account)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def login(self, username, password):


ChaseBank = Bank("Chase Bank")

ChaseBank.deposit(int(input("How much would you like to deposit? ")))
ChaseBank.withdraw(int(input("How much would you like to withdraw? ")))
