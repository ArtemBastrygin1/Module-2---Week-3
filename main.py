from functools import reduce

numbers = [1, 2, 5, 6, 8, -8, -10, 20]


def process_numbers(numbers):
    positive_numbers = list(filter(lambda x: x > 0 and x % 2 == 0, numbers))
    square_numbers = list(map(lambda x: x ** 2, positive_numbers))
    return reduce(lambda x, y: x + y, square_numbers)


print(process_numbers(numbers))

