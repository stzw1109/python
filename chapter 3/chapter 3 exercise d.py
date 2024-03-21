#option 1
def show_employee(name,salary):
    if salary== 0:
        print("name:",name, " salary:RM 3000")
    else:
        print("name:",name, " salary:RM ",salary)

show_employee("SAMUEL TAI",2000)

#option 2 (assigning default value)
def show_employee(name,salary):
    if salary== 0:
        print("name:",name, " salary:RM 3000")
    else:
        print("name:",name, " salary:RM ",salary)

show_employee("SAMUEL TAI",0)
