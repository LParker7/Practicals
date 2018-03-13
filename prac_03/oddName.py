name = input("What is your name? ")
while name == '':
    print('Invalid Input')
    name = input("What is your name? ")
for char in range(1,len(name),2):
    print(name[char])
