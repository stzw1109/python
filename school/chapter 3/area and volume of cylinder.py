import math

def area_cylinder(radius,height):
    return 2*(math.pi)*radius*height + 2*(math.pi)*(radius**2)

def volume_cylinder(radius,height):
    return (math.pi)*(radius**2)*height

radius = float(input("what is the radius of the cylinder:"))
height = float(input("what is the height of the cylinder:"))

print("area:",area_cylinder(radius,height))
print("volume:",volume_cylinder(radius,height))