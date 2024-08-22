numbers = [12, 75, 150, 180, 145, 525, 50]

for x in numbers:
    if x % 5 == 0 and x <=500 and x <= 150:
        print(x)
    elif x > 150 and x <=500:
        continue
    elif (x%5 != 0 or x%5 == 0) and x > 500 and x > 150:
        break