import math
side_length = float(input("Enter the side length of the hexagon: "))

def area_hexagon(side_length):
    area = (3*(math.sqrt(3))/2 * side_length**2)
    print("The area of the hexagon is: ",area)

area_hexagon(side_length)