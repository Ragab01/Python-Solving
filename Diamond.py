n=10
for i in range(n):
        # Print spaces
        print(' ' * (n - i - 1), end='')
        # Print stars
        print('* ' * (i + 1))
    
    # Lower half of diamond
for i in range(n-1, -1, -1):
        # Print spaces
        print(' ' * (n - i - 1), end='')
        # Print stars
        print('* ' * (i + 1))