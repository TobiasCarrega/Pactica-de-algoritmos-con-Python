#Metodo de burbujeo o de intercambio
def metododeintercambio(lista):
    desordenada = True
    while desordenada:
        desordenada = False
        for i in range(len(lista)-1):
            if lista[i]>lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                desordenada = True
    return lista

#metodo de insercion:
def metododeinsercion(lista):
    for i in range(1, len(lista)):# empieza en el 2º elemento
        aux = lista[i]
        j = i
        while j>0 and lista[j-1]>aux:
            lista[j] = lista[j-1]
            j = j - 1
        lista[j] = aux
    return lista


import random


#generar una lista
def crearListaRandom(): 
    lista=[]
    for i in range (10):
        num=int(random.randint(0, 99999))#generar un numero al azar
        lista.append(num)
    return lista


#Prueba de metodos en las listas
'''Primerlista=[77603, 23739, 99705, 95675, 34024, 20386, 67166, 64121, 93827, 54441]
segundaLista=[1862, 10143, 70651, 97889, 97506, 70569, 21601, 45482, 78986, 35836]
print(metododeinsercion(Primerlista))
print(metododeinsercion(segundaLista))'''

#generador de listas al azar ordenas:

def generadorDeListasOrdenas():
    lista1=crearListaRandom()
    metododeinsercion(lista1)
    lista2=crearListaRandom()
    metododeinsercion(lista2)

    return print("Lista1 \n",lista1,"\nLista2 \n",lista2)

print(generadorDeListasOrdenas())

