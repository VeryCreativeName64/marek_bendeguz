import random

def masodik():
    lista=[]
    for i in range(1,6):
        szam=(random.randint(1,10))
        print(szam,"!",end='')
    lista.append(szam)
    return lista


    