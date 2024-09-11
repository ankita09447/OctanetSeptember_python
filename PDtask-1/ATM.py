import time

# Card details
password = 1234
balance = 1000
history = []

# User PIN input
pin = int(input("Enter your PIN: "))

if pin == password:
    while True:
        print("""
            1 = Account Balance Inquiry
            2 = Cash Withdrawal
            3 = Cash Deposit
            4 = PIN Change
            5 = Transaction History
            6 = Exit
        """)
        try:
            option = int(input("Please choose an option: "))
        except ValueError:
            print("Please choose a valid option.")
            continue  # If invalid input, ask for the input again

        # Account balance inquiry
        if option == 1:
            print(f"Your current balance is: {balance}")
        
        # Cash Withdrawal
        elif option == 2:
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                print(f"{amount} withdrawn successfully.")
                history.append(f"Withdrawn: {amount}")

        # Cash Deposit
        elif option == 3:
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print(f"{amount} deposited successfully.")
            history.append(f"Deposited: {amount}")

        # PIN Change
        elif option == 4:
            new_pin = input("Enter your new PIN: ")
            pin = new_pin
            print("PIN changed successfully.")
            history.append("PIN changed")

        # Transaction History
        elif option == 5:
            print("Transaction History:")
            if history:
                for transaction in history:
                    print(transaction)
            else:
                print("No transactions yet.")

        # Exit
        elif option == 6:
            print("Exiting ATM.")
            break

        else:
            print("Invalid option. Please choose again.")
else:
    print("Incorrect PIN. Access denied.")
