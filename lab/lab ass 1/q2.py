vehicle = input("enter type of vehicle: ")
hours = int(input("enter number of hours: "))
sum = 0

def parking_rate_car(sum,hours):
    if hours <= 3:
        price = 1
        sum = sum + (price*hours)
        print("Total parking fee is:RM ",sum)
    elif hours > 3:
        price = 1.5
        sum = sum + (price*(hours-3)) + 3
        print("Total parking fee is:RM ",sum)

def parking_rate_lorry(sum,hours):
    if hours <= 3:
        price = 1.5
        sum = sum + (price*hours)
        print("Total parking fee is:RM ",sum)
    elif hours > 3:
        price = 2.5
        sum = sum + (price*(hours-3)) + 4.5
        print("Total parking fee is:RM ",sum)

def parking_rate_bus(sum,hours):
    if hours <= 3:
        price = 2
        sum = sum + (price*hours)
        print("Total parking fee is:RM ",sum)
    elif hours > 3:
        price = 3.5
        sum = sum + (price*(hours-3)) + 6
        print("Total parking fee is:RM ",sum)       

if vehicle == "C" or vehicle == "c":
    parking_rate_car(sum,hours)
elif vehicle == "L" or vehicle == "l":
    parking_rate_lorry(sum,hours)
elif vehicle == "B" or vehicle == "b":
    parking_rate_bus(sum,hours)
else:
    print("Invalid vehicle type")
    
