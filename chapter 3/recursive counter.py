def countdown(counter):
    if counter<=0:
        print("Stop!!")
    else:
        print(counter)
        countdown(counter-1)

counter = int(input("What number would you like to count from:"))
countdown(counter)