e=0
o=0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
for i in numbers:
    if i%2==0:
        e+=1
    else:
        o+=1

print(f"Number of even numbers : {e}")
print(f"Number of odd numbers : {o}")