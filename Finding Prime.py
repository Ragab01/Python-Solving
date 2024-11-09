start = 1
end = 15

primes = []

for num in range(max(2, start), end + 1):  # Start from max(2, start) to handle cases where start < 2
    is_prime = True
    
    # Only need to check up to the square root of num
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        primes.append(num)

print(primes)