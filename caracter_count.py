inputStr = input("enter the string - ")
charCount ={}

for c in inputStr:
    if c.isalpha():
        if c in charCount:
            charCount[c] += 1
        else:
            charCount[c] = 1

print(charCount)