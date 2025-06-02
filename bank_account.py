#my code
class BankAccount:
    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = balance
           
    def display_account(self):
        print(f"Account Number: {self.accountNumber}")
        print(f"Account Balance:{self.balance}")
        
    def deposit_money(self, deposit):
        self.deposit = deposit
        newAmount = self.balance + deposit
        print(f"Deposit: {deposit}")
        print(f"The new balance with deposit is {newAmount}")
         
    def withdraw_amount(self, withdrawal):
        self.withdrawal = withdrawal
        currentbalance = self.balance - withdrawal
        if withdrawal > currentbalance:
            print("Insufficient funds")
        else:
            print(f"Withdrew: {withdrawal}")
            print(f"The current balance after withdrawal is {currentbalance}")
        
class SavingsAccount(BankAccount):
    def display_account(self):
        interest = (3 / 100) * self.balance
        newbalance = interest + self.balance
        print(f"Account Number: {self.accountNumber}")
        print(f"Account Balance:{self.balance}")
        print(f"Interest: {interest}")
        print(f"Total Balance = {newbalance}")
               
class CurrentAccount(BankAccount):    
    def withdraw_amount(self, withdrawal):
        print(f"Withdrew: {withdrawal}")
        if withdrawal >= self.balance:
            newBalance = withdrawal  # in current account a customer can withdraw mrethan they have on the account 
            print("Exceeded overdraft limit")
        else:
            newBalance = self.balance - withdrawal
            print(f"Amount left: {newBalance}")
            
            
sav = SavingsAccount("SV00000456", 50000)
cur = CurrentAccount("CU00000222", 35000)

sav.display_account()
sav.deposit_money(10000)
sav.withdraw_amount(15000)

print("\n")
print("-"*30)
print("\n")

cur.display_account()
cur.deposit_money(5000)
cur.withdraw_amount(40000)

"""
#Lecturer's code
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited {amount}. New balance: {self.balance}')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'Withdrew {amount}. New balance: {self.balance}')

        else:
            print('Insufficient funds. ')

    def display_balance(self):
        print(f'Account {self.account_number} Balance: {self.balance}')


# subclass : Saving account
class SavingAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)

        self.interest_rate = interest_rate  # Store the interest rate

    # Add new method for interest rate calculation
    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        # Add the interest
        self.balance += interest
        print(f'Interest of {interest} added. New balance: {self.balance}')


# Child class : Current account
class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit  # Store overdraft

        # Override withdraw method to allow overdraft

        def withdraw(self, amount):
            if amount <= self.balance + self.overdraft_limit:
                self.balance -= amount
                print(f'Withdrew {amount}. New balance: {self.balance}')

            else:
                print('Exceeded the overdraft limit.')


# Create objects

saving = SavingAccount('SAV0555555', 100000, 5)
current = CurrentAccount('CUR0577777', 50000, 10)

# Test Method display
saving.display_balance()
saving.add_interest()
saving.withdraw(20000)
print(' LB ____________________')

current.display_balance()
current.withdraw(70000)
current.withdraw(45000)
"""