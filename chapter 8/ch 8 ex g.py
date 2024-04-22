file = open('word.txt', 'r')
f = file.readlines()

newlist = []

def func_1(newlist,f):
    for line in f:
        if line[-1] == '\n':
            newlist.append(line[:-1])
        else:
            newlist.append(line)
    print(newlist)

def func_2(newlist,f):
    for line in f:
        if line[-1] == '\n':
            f = f+[line[:-1]]
        else:
            f = f+[line]
    print(newlist)

func_1(newlist,f)
func_2(newlist,f)