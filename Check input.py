user_input = input("Enter Number Greater than 10")

while True:
    if int(user_input) <= 10:
        print("Invalid input. Number Greater than 10")
        user_input = input("Enter Number Greater than 10")
    else :
        break

print("You entered:", user_input)
