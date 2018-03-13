"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""
random_number = input("Please enter a number: ")
finished = False
result = 0
while not finished:
    try:
        random_number = 0
        random_number = int(input("Please enter a number: "))
        pass
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
