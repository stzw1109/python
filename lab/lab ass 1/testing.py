numbers = int(input("enter 3 numbers: ").split())
numbers = [int(num) for num in numbers]

def find_max(numbers):
    max = numbers[0]

    for x in numbers:
        if numbers[x] > max:
            max = numbers[x]

    print("The maximum number is: ",max)

find_max(numbers)