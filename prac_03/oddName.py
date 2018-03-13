def main():
    name = get_name()
    interval = get_interval()
    extract_letters(name, interval)


def get_name():
    name = input("What is your name? ")
    while name == '':
        print('Invalid Input')
        name = get_name()
    return name


def get_interval():
    interval = int(input("What is the counting interval? "))
    while interval < 0:
        print('Invalid Input')
        interval = get_interval()
    return interval


def extract_letters(name, interval):
    for char in range(0, len(name), interval):
        print(name[char])


main()