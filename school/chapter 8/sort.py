
numbers = []
count_even = 0
count_odd = 0
count_zero = 0
sum_of_nums = 0
count_negative = 0

# Loop to allow the user to input numbers
while True:
    # Prompt the user to enter a number or 'q' to quit
    user_input = input("Enter a number (or 'q' to quit): ")
    
    # Check if the user wants to quit
    if user_input == 'q' or user_input == 'Q':
        break
    
    # Convert the input to an integer and add it to the list
    number = int(user_input)
    numbers.append(number)
    sum_of_nums += 1

    if number < 0:
        count_negative+=1
    elif abs(number) % 2 == 0 and number != 0:
        count_even+=1
    elif abs(number) % 2 != 0:
        count_odd+=1
    elif int(number) == 0:
        count_zero+=1
        
# Sort the list of numbers
numbers.sort()

# Print the sorted list
print("Sorted numbers:", numbers)
print("Even numbers:", count_even)
print("Odd numbers:", count_odd)
print("Zero numbers:", count_zero)
print("Negative numbers:", count_negative)
print("Sum of numbers:", sum_of_nums)