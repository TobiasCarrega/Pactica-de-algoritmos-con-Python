#Escribir un algoritmo que lea numeros enteros hasta que se ingrese un 0, y muestre el promedio y la cantidad de numeros ingresados

# sumador=0
# contador=0
# n_ingresado=int(input("Ingrese un numero entrero para sumar y sacar promedio o introduzca 0 para terminar "))
# while n_ingresado != 0:
#     sumador=sumador+n_ingresado
#     contador=contador+1
#     n_ingresado=int(input("ingrese otro numero o 0 para terminar "))

# if sumador > 0:
#     print("El promedio es ",sumador/contador,"y se ingresaron",contador,"numeros")    
# else:    
#     print("No ingresaste ningun valor")




# Introduzca un numero y indique la sumatoria


'''contador=0
sumador=0
numeros=int(input("sumar los numeros hasta ingresar 0: "))

while numeros != 0:
    sumador= sumador+numeros
    numeros=int(input("ingrese otro numero o 0 para terminar "))

if sumador>0:
    print("la suma de los numeros ingresados es de: ",sumador)
else:
    print("no ingresaste numeros necesarios")'''


rango=175-42
iniciador=42
sumatoria=43
contador=0
for numero in range(rango):
    iniciador=iniciador+1
    sumatoria=sumatoria+iniciador
    contador+=1
    print(sumatoria)

print(contador)


