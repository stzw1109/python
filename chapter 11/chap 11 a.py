keys = ['ten','twenty','thirty']
values = [10,20,30]
result = dict()

for i in range(len(keys)):
    result.update({keys[i]:values[i]})


print(result)