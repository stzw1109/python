num = [[1,2],[3],[4,5,6]]

def nested_sum(num):
    total = 0
    for i in num:
        if isinstance(i, list):
            total += nested_sum(i)
        else:
            total += i
    return total

print(nested_sum(num))
