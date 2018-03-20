import random


def main():
    number_of_rows = int(input("How many quick picks? "))
    for row in range(number_of_rows):
        quick_pick = get_quick_pick()
        quick_pick_string = ' '.join(str(number) for number in quick_pick)
        print(quick_pick_string)


def get_quick_pick():
    quick_pick = []
    for column in range(6):
        random_integer = random.randint(1, 45)
        while random_integer in quick_pick:
            random_integer = random.randint(1, 45)
        quick_pick.append(random_integer)
    quick_pick.sort()
    return quick_pick


main()
