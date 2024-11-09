word=input("Enter a Word to reverse It").strip()
reversed_word=""

for i in range (len(word)-1 , -1 , -1):
    reversed_word+=word[i]

print(reversed_word)