marks = float(input("enter marks: "))

def marks_category(marks):
   if marks >= 75:
      print("First grade")
   elif 70 <= marks < 75:
      print("Second grade")
   elif 60 <= marks < 70:
      print("Second")
   elif 50 <= marks < 60:
      print("Third")
   elif 45<= marks < 50:
      print("F1 Supp")
   elif 40 <= marks < 45:
      print("F2")
   elif marks < 40:
      print("F3")

marks_category(marks)  
            
   