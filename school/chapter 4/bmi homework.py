weight = float(input("Enter weight: "))
height = float(input("Enter height: "))
age = int(input("Enter age: "))

def bmi(weight, height):
      bmi = weight / (height ** 2)
      return bmi
bmi_result = bmi(weight, height)

def bmi_category(bmi_result):
      if bmi_result < 18.5:
         return "Underweight"
      elif 18.5 <= bmi_result < 24.9:
         return "Normal weight"
      elif 25 <= bmi_result < 29.9:
         return "Overweight"
      elif bmi_result >= 30:
         return "Obese"
      else:
         return "Invalid weight or height"

def bmi_warning(bmi_result,age):
   if bmi_result not in range(19,25) and age in range(19,25):
         return "Warning: BMI out of normal range. Must be between 19 and 24"
   elif bmi_result not in range(20,24) and age in range(25,35):
         return "Warning: BMI out of normal range. Must be between 20 and 25"
   elif bmi_result not in range(21,27) and age in range(35,45):
         return "Warning: BMI out of normal range. Must be between 21 and 26"
   elif bmi_result not in range(22,28) and age in range(45,55):
         return "Warning: BMI out of normal range. Must be between 22 and 27"
   elif bmi_result not in range(23,29) and age in range(55,65):
         return "Warning: BMI out of normal range. Must be between 23 and 28"
   elif bmi_result not in range(24,30) and age >=65:
         return "Warning: BMI out of normal range. Must be between 24 and 29"
        
print("""\nBMI value: {}
BMI category:{}
Age:{}
Note: {}
         """.format(bmi_result,bmi_category(bmi_result),age,bmi_warning(bmi_result,age))
      )  
          