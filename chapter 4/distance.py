import math

x1 = float(input("enter x1 coordinate:"))
y1 = float(input("enter y1 coordinate:"))

x2 = float(input("\nenter x2 coordinate:"))
y2 = float(input("enter y2 coordinate:"))

def distance_calculation(x1,x2,y1,y2):
    first_variable = (x2 - x1) ** 2
    second_variable = (y2 - y1) ** 2

    sum = first_variable + second_variable

    distance = math.sqrt(sum)

    print("\nDistance=",distance)


distance_calculation(x1,x2,y1,y2)