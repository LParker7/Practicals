# 1
name = input("What is your name? ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

# 2
in_file = open("name.txt", 'r')
name = in_file.read()
print("Your name is", name)
in_file.close()

# 3
in_file = open("numbers.txt", 'r')
number1 = int(in_file.readline())
number2 = int(in_file.readline())
print(number1 + number2)
in_file.close()

# 4
in_file = open("numbers.txt", 'r')
total = 0
for line in in_file:
    number = int(line)
    total += number
print(total)
in_file.close()
