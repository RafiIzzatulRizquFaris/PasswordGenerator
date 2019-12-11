import random
chars = '1234567890!@#$%^&*()_+qwertyuiop[]\{}|asdfghjkl;'"zxcvbnm,./<>?`~"
inputMuchPassword = input("input how much password do you want")
inputMuchPassword = int(inputMuchPassword)
inputLength = input("input your password length prefference?")
inputLength = int(inputLength)
for p in range(inputMuchPassword):
    password = ''
    for c in range(inputLength):
        password += random.choice(chars)
    print(password)