def bmi_calculation(weight,height):
    bmi = weight/(height**2)
    return bmi

weight = float(input("What is your weight:"))
height = float(input("What is your height:"))

results = bmi_calculation(weight,height)

print(results)