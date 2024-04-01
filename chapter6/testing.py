num = 6

for x in range(0,5):
    for y in range(1,6-x,1):
        print(num-y,end=" ")
    print()    
    num-=1