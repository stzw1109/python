t = [1,2,3,4]

def chop(t):
    t.remove(t[0])
    t.remove(t[-1])
    return t

print(chop(t))