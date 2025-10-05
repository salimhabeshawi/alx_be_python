class BankAccount:
    def __init__(self, account_balance, initial_balance = 0):
        self.account_balance = account_balance
        self.initial_balance = initial_balance

    def deposit(self, amouunt):
        self.account_balance += amouunt
    def withdraw(self, amouunt):
        if self.account_balance >= amouunt:
            self.account_balance -= amouunt
            return True
        else:
            return False
    def display_balance(self):
        print(f"current Balance: ${self.account_balance}")
    