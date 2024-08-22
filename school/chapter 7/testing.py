layout = "{0:>10}{1:>10}{2:>10}{3:>10}{4:>10}"

print(layout.format("1", "2", "3", "4", "5"))

for i in range(5):
    print(layout.format(i,i+2,i+3,i+4,i+5),end = " ") 