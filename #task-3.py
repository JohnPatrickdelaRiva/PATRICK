class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance is ${self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}.")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")
    def display_balance(self):
        print(f"Account balance: ${self.balance:.2f}")

account = BankAccount("120800", "ADRIAN", 700000)

account.deposit(50000)
account.withdraw(900)
account.withdraw(600)  

account.display_balance()