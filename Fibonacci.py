n = int(input("How many Fibonacci"))

a = 0
b = 1

print("Fibonacci sequence:")
for i in range(n):
    print(a, end=" ")

    a, b = b, a + b