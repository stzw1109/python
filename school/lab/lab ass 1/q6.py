numbers = input("Enter 3 numbers: ").split()
numbers = [int(num) for num in numbers]

def find_max(numbers):
    max_num = numbers[0]

    for x in numbers:
        if x > max_num:
            max_num = x

    print("The maximum number is: ", max_num)

find_max(numbers)

