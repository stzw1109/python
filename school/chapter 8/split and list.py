name = input("enter a name: ")
def splitting(name):
    t = name.split()
    print(t)

def listing(name):
    z = list(name)
    print(z)    

def deleting(name):
    x = name.pop(1)
    print("popped:",x)
    
    del name[2:4]
    print("after deletion:",name)

    name.remove('i')
    print("after removing:",name)

splitting(name)
listing(name)   
deleting(name)