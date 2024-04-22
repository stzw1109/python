a = [1,2,2]
b =['b','a']

def is_sorted(x):
    return x == sorted(x)

print(is_sorted(a))
print(is_sorted(b))