'''N=[1,2,3,4,5,6,7,8,9,10]
i=9
for i in range (10):
    print(N[i])
    i-=1'''

'''lista=[1,2,3,4,5,6,7,8,9,10]
for numero in lista:
    print(numero)'''


#Leer 5 numeros enteros, clacular su promedio e imprimir aquellos valores leidos que sean mayores al promedio obtenido
'''numeros=[]
mayores=[]
promedio=0

for i in range (5):
    numero=int(input("ingrese un numero: "))
    numeros.append(numero)
    promedio+=numero

promedio=promedio/5
if numero>promedio:
    mayores.append(numero)
print(numeros,promedio,mayores)
print("los numeros mayores al promedio son: ", mayores)'''


'''promedio=numeros/5
if numero>promedio:
    print(numero)'''


'''def crearLista(n):
    lista = []
    for i in range(n):
        numero = int(input("Ingrese un número: "))
        lista.append(numero)
    return lista
n=int(input("ingrese la cantidad de elementos a gregar en la lista: "))
# crearLista(n)
print("la lista creada es:", crearLista(n))
'''


# Ejercicio 1: Escribir una función que solicite ingresar una serie de números entre a y b y guardarlos en una   lista. En caso de ingresar un valor fuera de rango el programa mostrará un mensaje de error y  solicitará un  nuevo número. Para finalizar la carga se deberá ingresar -1. La función no recibe  ningún parámetro, y devuelve la lista cargada (o vacía, si el usuario no ingresó nada) como  valor de retorno.   
def numerosEntreLimites():   
    n=0
    a=int(input("ingrese el primer limite: "))
    b=int(input("ingrese el segundo limite: "))
    lista=[]
    while n!=-1:
        if a>n<b or b>n<a: #a<n>b or b<n>a:
            n=int(input("ingrese un numero: "))
            lista.append(n)
        else:
        print("¡Debe ingresar un numero dentro de los limites!")
    return lista
numerosEntreLimites()