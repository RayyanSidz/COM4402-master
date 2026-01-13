Balance = 100.0
while True:
    withdrawal_amount = int(input("Enter withdrawal amount: "))
    if withdrawal_amount == 0 or Balance == 0.0:
        print("exiting")
        break
    elif withdrawal_amount <= Balance:
        Balance -= withdrawal_amount
        print(Balance)
    else:
        print("Insufficient funds")