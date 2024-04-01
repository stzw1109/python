numbers = [12,75,150,180,145,525,50]

for x in range(0,7):
    if numbers[x] % 5 == 0:
        print(numbers[x])
    elif numbers[x] > 500:
        print("The number is greater than 500")
        break
    elif numbers[x] >150:
        continue