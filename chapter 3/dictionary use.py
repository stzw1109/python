def square(x):
    return x**2
def cube(x):
    return x**3

dictionary = {'square_result':square,'cube_result':cube}

print(dictionary['square_result'](3))
print(dictionary['cube_result'](5))