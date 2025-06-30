#ingresar un rango de años y mostrar la cantidad de añños bisiestos hay en medio
'''
year=0
inicio=int(input("ingrese el año de inicio"))
fin=int(input("ingrese el año de fin"))

for year in range(inicio,fin):
    '''



#Dado un número N, generar y mostrar: Los primeros N términos de la serie: 1, 7, 19, 43, 91... (cada término = 2 * anterior + 5). La suma total de los términos generados. Validar que N sea positivo.

'''n=int(input("ingrese un numero limite"))
acumulador=1
suma=0

for i in range(n):
    suma+=acumulador
    acumulador=2*suma+5
    print(acumulador)'''



#Sistema de gestion de notas|ingresar legajo|-1 para terminar|ingresar nota final|determinar cuantos estan aprobados nota>=4, desaprobados  nota<4 y porcentaje de aplazados

legajo=int(input("ingrese numero de legajo(-1 para terminar)"))
nota=float(input("ingrese nota final"))

alumnos=0
aprobados=0
desaprobados=0
aplazados=0
promedio_aplazados=0

while legajo!=-1:
    if 1<nota<=10:
        if nota>=4:
            aprobados+=1
        else:
            desaprobados+=1
    elif nota==1:
        aplazados+=1
    else:
        print("nota invalida")
    alumnos+=1
    legajo=int(input("ingrese numero de legajo(-1 para terminar)"))
    if legajo !=-1:
        nota=float(input("ingrese nota final"))
else:
    print("alumnos aprobados", aprobados)
    print("alumnos desaprobados",desaprobados)
    promedio_aplazados=(aplazados*100)/alumnos
    print("promedio de alumnos aplazados",promedio_aplazados)