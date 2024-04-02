name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

length = min(len(name1), len(name2))

for x in range(length):
    for y in range(length):
        print(name1[x])
        print(name2[x])
        break
