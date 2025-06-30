# Inicialización de listas
legajos = []
notas = []

#1. Complete la condición y lo necesario para que funcione; y explique el propósito del ciclo while
legajo=0
while legajo!=-1:
    legajo = int(input("Ingrese número de legajo (-1 para terminar): "))
    
    if legajo!=-1:
        while legajo <= 0:
            print(" El número de legajo debe ser positivo.")
            legajo = int(input("Ingrese número de legajo de nuevo (-1 para terminar): "))


        nota = int(input("Ingrese nota del examen final (1 a 10): "))
        while nota < 1 or nota > 10:
            print(" Nota inválida. Debe estar entre 1 y 10.")
            nota = int(input("Ingrese nota válida del examen final: "))

        legajos.append(legajo)
        notas.append(nota)

print (legajos, notas)

# Análisis de datos
aprobados = 0
desaprobados = 0
suma_notas = 0

for nota in notas:
    if nota >= 4:
        aprobados += 1
    else:
        desaprobados += 1
    suma_notas += nota

#2. Explique que hace esta parte del código
# guarda la cantidad de valores que existe en la lista "notas" en la variable "cantidad_estudiantes" y si esa cantidad es mayor a 0, calcula el promedio de las notas
cantidad_estudiantes = len(notas)
if cantidad_estudiantes > 0:
    promedio = suma_notas / cantidad_estudiantes
else:
    promedio = 0

#2.2 Explique que hace esta parte del codigo
# Crea la lista "superan_promedio" para guardar el numero de legajo de aquellar personas  que estan por encima del promedio mediante un fr recorriendo las listas, usando el contador del for para sincornizar la nota con los legajos.
superan_promedio = []
for i in range(cantidad_estudiantes):
    if notas[i] > promedio:
        superan_promedio.append(legajos[i])

#3. Explique que hace esta parte del codigo
#Recorre una sola vez la lista completa de legajos y la ordena de menor a mayor modificando la lista de legajos y sus respectivas notas
for i in range(len(legajos) - 1):
    for j in range(i + 1, len(legajos)):
        if legajos[i] > legajos[j]:
            legajos[i], legajos[j] = legajos[j], legajos[i]
            notas[i], notas[j] = notas[j], notas[i]

# Mostrar resultados
print("\n Resultados:")
print(f" Estudiantes aprobados: {aprobados}")
print(f" Estudiantes desaprobados: {desaprobados}")
print(f" Promedio general de notas: {promedio:.2f}")
print(f" Legajos que superaron el promedio: {superan_promedio}")
print(f" Legajos ordenados ascendentemente: {legajos}")

#4. Que tipo de búsqueda realiza? Proponer otra solución
buscar=0
while buscar!=-1:
    buscar = int(input("\n Ingrese un número de legajo para consultar la nota: (-1 para terminar)"))
    inicio = 0
    fin = len(legajos) - 1
    encontrado = False

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if legajos[medio] == buscar:
            print(f" Legajo {buscar} tiene nota: {notas[medio]}")
            encontrado = True
        elif buscar < legajos[medio]:
            fin = medio - 1
        else:
            inicio = medio + 1

    if not encontrado:
        print(" Legajo no encontrado.")