N=int(input("guess a number between 1 and 9").strip())
while True:
    if N in range (1,10):
        print("Well guessed!")
        break
    else:
        N=int(input("guess a number between 1 and 9").strip())
