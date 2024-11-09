balance = 1000.0 
amount = float(input("Enter the amount to withdraw: $"))

    
if amount <= 0:
        print("Invalid amount. Please enter a positive value.")
    
    
elif amount > balance:
        print("Insufficient funds!")
else:
        balance -= amount
        print(f"Transaction successful! You withdrew ${amount}.")
        print(f"Remaining balance: ${balance}")