sum=0
avr=0
i=1
while True:
    N=int(input("Enter Number").strip())
    if N == 0:
        break
    sum +=N
    avr = sum/i
    i+=1

print(f"sum : {sum}")
print(f"average : {avr}")