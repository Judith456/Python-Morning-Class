password = 1234
amount = 30000
account_minimum_balance = 10000

withdrawAmount = int(input("Enter amount to be withdraw: "))
entered_password = int(input("Enter password: " ))

if entered_password != password:
        print("Incorrect password")
        exit()
    
def display_amount():
    print("Account Balance: ", amount)
    
def withdraw_amount():
    global amount
    if withdrawAmount >= amount:
        print("Insufficient Balance")
       
    elif (amount - withdrawAmount) < account_minimum_balance:
        print("Cannot Withdraw: Minimum balance of", account_minimum_balance, "must be maintained")
    else:
        amount -= withdrawAmount
        print("Withdrawal successful")
        print("New Balance: ", amount)

while True:
    print("\nWithdawal Options")
    print("1. Check Account balance")
    print("2. Withdraw Amount")
    print("3. Exit")
    print("\n")
    choice = input("Enter option number: ")
    
    
    if choice == '1':
       display_amount()
    elif choice == '2':
       withdraw_amount()
    elif choice == '3':
           print("Exited Successfully")
           break
    else:
        print("Invalid choice")
            
        
        
