Lista=[]

for i in range((101)):
    Lista.append(i)

for i in range(len(Lista)):
    if i % 5 == 0 and i % 3 == 0:
        oszt = i
        H = Lista.index(oszt)
        Lista[H] = "Fizz"+"Buzz"
    elif i % 3 == 0:
        oszt = i
        H = Lista.index(oszt) 
        Lista[H] = "Fizz"
    elif i % 5 == 0:
        oszt = i
        H = Lista.index(oszt) 
        Lista[H] = "Buzz"

Lista.remove(Lista[0])
print(Lista)