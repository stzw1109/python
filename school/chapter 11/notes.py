utem = {1:"yeehai",2:"digga"}

print(utem)

newUtem = dict()
print (newUtem)

newUtem['samuel']='is digga'

print(newUtem)

menu ={'milo':10, 'nasi lemak':20, "teh ais":30,'oni':9999,'ais kacang':50}

print(menu)

print(menu['milo'])

print(len(menu))

del menu['nasi lemak']
print(menu)

menu['milo']+=15
print(menu)

menu1 = menu
menu1['milo']+=5 
print(menu1)

menu2 = menu.copy()
menu['milo']+=5
print("menu: ",menu)
print("menu1: ",menu1)
print("menu2: ",menu2)

menu['teh ais'] = 'free'
print("menu: ",menu)
print("menu1: ",menu1)
print("menu2: ",menu2)

letsort = list(menu.keys())
letsort.sort()
afterSort = {i:menu[i] for i in letsort}
print(afterSort)

alist = [1,2,3,4]
aTuple = (5,6,7,8,9)

newList = list(zip(alist,aTuple))
print(newList)

newTuple = dict(zip("alist","aTuple"))
print(newTuple)