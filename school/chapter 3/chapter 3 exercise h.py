def time_determiner(current_time):
    if current_time < 12 and current_time >= 0:
        print("The time when the alarm is triggered: ", float(current_time), " AM")
    else:
        print("The time when the alarm is triggered: ", float(current_time - 12), " PM")

def time_calculator(current_time,remaining_hours,initial_time,max_time):
    while remaining_hours > 0:
        if current_time == max_time:
            current_time = initial_time
        else:
            current_time +=1
            remaining_hours-=1
            
    time_determiner(current_time)

current_time = float(input("What is the time now(24 hr system):"))
remaining_hours = float(input("How long before alarm is triggered:"))

time_calculator(current_time,remaining_hours,0,24)


#second option
def time_determiner(current_time):
    if current_time < 12:
        print(f"current time:{current_time}AM")
    else:
        print(f"current time:{current_time - 12} PM")

def time(current_time,hours,max_hour):
    while hours>0:
        if (current_time < max_hour):
            current_time = current_time + 1
        else:
            current_time = 0
            current_time = current_time + 1
        hours -= 1
    time_determiner(current_time)

max_hour = 24
current_time = float(input("enter current time(24hr):"))
hours = float(input("enter hours: "))

time(current_time,hours,max_hour)
    