def outer(a,b):
    
    def inner(a,b):
        return a+b
    sum = inner(a,b) + 5

    print(sum)

outer(1,2)

