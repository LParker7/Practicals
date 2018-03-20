def main():
    numbers = get_numbers()
    evaluate_numbers(numbers)


def get_numbers():
    numbers = []
    for number in range(5):
        input_number = int(input("Number: "))
        numbers.append(input_number)
    return numbers


def evaluate_numbers(numbers):
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    numbers.sort()
    print("The smallest number is {}".format(numbers[0]))
    print("The largest number is {}".format(numbers[-1]))
    average = get_average(numbers)
    print("The average of the numbers is {}".format(average))


def get_average(numbers):
    sum_of_numbers = 0
    for number in range(5):
        sum_of_numbers += numbers[number - 1]
    average = sum_of_numbers / 5
    return average


main()
