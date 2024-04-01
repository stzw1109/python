numbers = [12, 75, 150, 180, 145, 525, 50]
count = 0
while count <= 6:
    if numbers[count] % 5 == 0 and numbers[count] <= 150 and numbers[count] <= 500:
        print(numbers[count])
    elif numbers[count] > 150:
        continue
    elif numbers[count] > 500:
        print("The number is greater than 500")
        break
    count +=1
