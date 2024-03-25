def day(day_num):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
   
    if 0 <= day_num <= 6:
        print(days[day_num])
    else:
        print("Invalid day number")

day_num = int(input("Enter day number: "))
day(day_num)