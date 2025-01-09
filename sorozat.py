import random

def masodik():
    lista=[]
    for i in range(1,6):
        szam=(random.randint(1,10))
        lista.append(szam)
    print(*lista,sep="!")
    return lista

def nagyobb(lista):
    db=0
    for i in range(1,len(lista)):
        if lista[i] > lista[i-1]:
            db+=1
    return db

def konzol_kiir(eredmeny):
    print("II/D,E:")
    print(f"Nagyobb számok száma: {eredmeny}")
    


    