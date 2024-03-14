current_time = 14.00
remaining_hours = 51

initial_time = 0
max_time = 24

while remaining_hours > 0:
    if current_time == max_time:
        current_time = initial_time
    else:
        current_time +=1
        remaining_hours-=1

actual_time = current_time - 12

if current_time < 12 and current_time >= 0:
    print("the current time after 51 hours is ", float(actual_time), " AM")
else:
    print("the current time after 51 hours is ", float(actual_time), " PM")