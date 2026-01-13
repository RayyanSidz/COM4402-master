# ATM Helper Functions
def show_menu():
     print("1. Deposit")
     print("2. Withdraw")
     print("0. Exit")
     choice = input("Enter choice: ")
     return choice
def deposit(balance):
     amount = float(input("Amount to deposit: "))
     # TODO: if amount > 0, update balance; otherwise print an error
     if amount > 0:
         balance += amount
     else:
         print("Error")
     # TODO: return the (possibly) updated balance
     return balance
def withdraw(balance):
     amount = float(input("Amount to withdraw: "))
     # TODO: check amount > 0 and amount <= balance
     if amount > 0 and amount <= balance:
        # TODO: update balance only if valid
        balance -= amount
     # TODO: return balance
     return balance

balance = 0.0

while True:
    choice = show_menu()
    if choice == "1":
        balance = deposit(balance)
        print(balance)
    elif choice == "2":
        balance = withdraw(balance)
        print(balance)
    elif choice == "0":
        print("exited")
        break
    else:
        print("Invalid input")

