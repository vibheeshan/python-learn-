
balance = 5000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Choose option: "))

    if choice == 1:
        print("Balance:", balance)

    elif choice == 2:
        amount = int(input("Enter deposit: "))
        balance += amount
        print("New balance:", balance)

    elif choice == 3:
        amount = int(input("Enter withdrawal: "))
        if amount <= balance:
            balance -= amount
            print("Remaining balance:", balance)
        else:
            print("Insufficient balance")

    elif choice == 4:
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice")
