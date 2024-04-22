t = [1,2,3]
def cumsum(t):
    for i in range(len(t)-1):
        t[i+1] = t[i+1]+t[i]
    print(t)

cumsum(t)