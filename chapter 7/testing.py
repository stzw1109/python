layout = "{0:>6}{1:>6}{2:>6}{3:>6}{4:>6}{5:>6}{6:>6}{7:>6}{8:>6}{9:>6}{10:>6}{11:>6}{12:>6}"

print(layout.format("\t","1", "2", "3", "4", "5", "6", "7","8","9","10","11","12"))
print("-----------------------------------------------------------------------------------")

for x in range(1,13):
    print("{0:>2} :".format(x), end="")
    for y in range(1,13):
        print("{0:>6}".format(x*y), end="")
    print()