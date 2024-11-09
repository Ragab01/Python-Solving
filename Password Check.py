correct_password = "password123"
attempts = 3

while attempts > 0:
    entered_password = input("Enter password: ")
    if entered_password == correct_password:
        print("Access granted.")
        break
    else:
        attempts -= 1
        print("Incorrect password. Attempts left:", attempts)

if attempts == 0:
    print("Access denied.")
