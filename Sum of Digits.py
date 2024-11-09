number = 12345  # Example number
sum_of_digits = 0

while number > 0:
    sum_of_digits += number % 10
    number //= 10

print("Sum of digits is:", sum_of_digits)
