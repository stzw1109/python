
numbers = []
count_positive = 0
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
    
    if int(user_input) < 0:
        count_negative+=1
    else:
        count_positive+=1

# Sort the list of numbers
numbers.sort()

# Print the sorted list
print("Sorted numbers:", numbers)
print("Positive numbers:", count_positive)
print("Negative numbers:", count_negative)