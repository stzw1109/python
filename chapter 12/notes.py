a = (1,2,3,4,56)
print(a)

print(a[1:3])

name = tuple('samuel')
print(name)
baru = ('s',) + name[:5]
print(baru)

name2 = tuple('ankeetha')

name,name2 = name2,name
print(name)
print(name2)

name3 = ("samuel_tai")
first,last = name3.split("_")
print(first)
print(last)

maths = divmod(12,3)
print(maths)

divisor, remainder = divmod(12,3)  
print("divisor:",divisor)
print("remainder:",remainder)

values = (1111,123123,1,199999,69696969)

def min_max(values):
    return min(values),max(values)

min,max = min_max(values)

print("min:",min)
print("max:",max)