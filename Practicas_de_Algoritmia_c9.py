
#uso de las erramientas import y random: para usar el random siempre hay q importarlo 
import random

'''dado=0

for i in range(10):
    dado = random.randint(1,6)
    print(dado, end=" ")'''





#crear un conjunto de dados a tirar:

'''dado=[]
n=int(input("ingrese la cantidad de dados a tirar: "))
for i in range(n):
    tirada = random.randint(1,6)
    dado.append(tirada)
    print(f'\ndado{i+1}:', tirada)'''



#recorridos de listas(se busca copiar la lista x en la lista d)
'''
x=["l","u","n","e","s"]
d=[]

n=len(x)
for i in range(n):
    d.append(x[i])
print(d)'''


# recorrer la lista para buscar letras

'''x=["l","u","n","e","s"]
d=[]
e=0

n=len(x)
for i in range(n):
    if x[i]=="l":
        e+=1

print("cantidadd de veces que se repite 'e':", e)'''

#hacer una lista de numeros al azar del 1 al 100 donde la cantidad de elementos sera ingresada por el usuario. Luego se solicita leer un valor y biscarlo en la lista mediante una funcion, devolviendo su ubicacion o -1 si no se la encuentra


'''def buscarNumero():
    n=len(list)
    for i in range(n):
        if list[i]==numero:
            coincidencias.append(i)
    if coincidencias==[]:
        coincidencias.append(-1)
    return(coincidencias)

coincidencias=[]
list=[]

n=int(input("ingrese la cantidad de elemtos en su lista: "))
numero=int(input("ingrese el numero a buscar: "))


for i in range(n):
    list.append(random.randint(1,2))


print(list)
print(buscarNumero())'''

#ordenar los numeros de una lista:

'''lista=[2,7,5,1,6]

largo=len(lista)
for i in range(largo-1):
    for j in range(i+1,largo):
        if lista[i]>lista[j]:
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux

print(lista)'''


