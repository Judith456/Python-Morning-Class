"""
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))



#Use that function definition to make a function that always doubles and triples the number you send in:
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
"""

"""

🔴 Problems:
You're calling SavingsAccount() and CurrentAccount() without passing the required parameters (accountNumber, balance).

Methods like display_account() unnecessarily accept accountNumber and balance again, instead of using the values already stored in the object.

In deposit_money() and withdraw_amount(), the actual balance isn't being updated — you're just printing the result.

Redundant instance variables like self.deposit, self.withdrawal are unnecessary unless you're planning to access them elsewhere.

The BankAccount class methods should be properly inherited and reused, unless they’re intended to be overridden.

The CurrentAccount.withdraw_amount() method has strange logic — it assigns withdrawal to newBalance if withdrawal > balance, which doesn’t make sense.

✅ Fixed and Cleaned-up Version:
python
Copy code

class BankAccount:
    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = balance

    def display_account(self):
        print(f"Account Number: {self.accountNumber}")
        print(f"Balance: {self.balance}")

    def deposit_money(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")
        print(f"New Balance: {self.balance}")

    def withdraw_amount(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}")
            print(f"New Balance: {self.balance}")

class SavingsAccount(BankAccount):
    def display_account(self):
        interest = (3 / 100) * self.balance
        total_balance = self.balance + interest
        print(f"Account Number: {self.accountNumber}")
        print(f"Balance with Interest: {total_balance:.2f}")

class CurrentAccount(BankAccount):
    def withdraw_amount(self, amount):
        if amount > self.balance:
            print("Insufficient funds in current account")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}")
            print(f"New Balance: {self.balance}")
#✅ Example Usage:
#python
#Copy code

sav = SavingsAccount("SV00000456", 50000)
cur = CurrentAccount("CU00000321", 30000)

sav.display_account()
sav.deposit_money(10000)
sav.withdraw_amount(15000)

print("-"*30)

cur.display_account()
cur.deposit_money(5000)
cur.withdraw_amount(35000)
"""