

#Ejercicio 3:
#  Desarrollar un programa que solicite un número de mes (por ejemplo 4) y escriba el nombre del mes en letras ("abril"). Verificar que el mes sea válido y mostrar un mensaje de error en caso de que no lo sea.


'''num=int(input("Ingrese un numero "))
# if num>=1 and num<=12:
#     print("El mes es ")
if num==1:
    print("enero")
elif num==2:
    print("febrero")
elif num==3:
    print("marzo")
elif num==4:
    print("abril")
elif num==5:
    print("mayo")
else:
    print("No es un numero valido")   '''      





#Ejercicio 4:
#  En el congreso se vota una ley muy importante. Desarrollar un programa que permita ingresar la cantidad de votos a favor y en contra, e informe el porcentaje obtenido en cada

'''votos_si=float(input("ingrese cantidad de votos positivos "))
votos_no=float(input("Ingrese los votos negativos "))
total_votos=votos_si+votos_no
porcentaje_si=votos_si/(total_votos/100)
porcentaje_no=votos_no/(total_votos/100)
if porcentaje_si>votos_no:
    print("Aprobado con ",porcentaje_si,"% de los votos contra ",porcentaje_no,"% de votos negativos")
else:
    print("denegado con ",porcentaje_no,"% de los votos contra ",porcentaje_si,"% de votos negativos")'''




#Ejercicio 5: 
# Ingresar las notas de los dos parciales de un alumno e indicar si promocionó, aprobó o si debe recuperar. Informar un error si el valor de alguna nota no está  entre 0 y 10.
#  · Se promociona cuando las notas de ambos parciales son mayores o  iguales a 7.
#  · Se aprueba cuando las notas de ambos parciales son mayores o iguales  a 4.
#  · Se debe recuperar cuando al menos una de las dos notas es menor a 4.


'''parcial_1=float(input("ingere la nota del primer parcial "))
parcial_2=float(input("ingrese la nota del segundo parcial "))
promedio=(parcial_2+parcial_1)/2

if parcial_1<0 or parcial_1>10 or parcial_2<0 or parcial_2>10:
    print("no es una nota valida")
elif parcial_1>=7 and parcial_2>=7:
    print("promocionaste con ",promedio)
elif 7>parcial_1>=4 and 7>parcial_2>=4 :
    print("Aprobado con final obligatorio y promedio de ",promedio)
elif parcial_1<4 or parcial_2<4 :
    print("Desaprobado")'''




#Ejercicio 6:
#  Una editorial determina el precio de un libro según la cantidad de páginas que contiene. El costo básico del libro es de $5000, más $32 por página con encuadernación rústica.  Si el número de páginas supera las 300 la encuadernación  debe ser en tela, lo que incrementa el costo en $1200.  Además, si el número de  páginas sobrepasa las 600 se hace necesario un procedimiento especial de encuadernación que incrementa el costo en otros $3360. Desarrollar un programa que calcule el costo de un libro dado el número de páginas

'''paginas=int(input("Ingrese la cantidad de paginas "))
precio=5000+32*paginas
if paginas>600:
    precio=precio+3360
    print("El precio con encuadernado especial es de $",precio)
elif paginas>300:
    precio=precio+1200
    print("El precio con encuadenado en tela es de $",precio)
else:
    print("El precio del libro basico es de $",precio)'''




# Ejercicio 7:
#  Un fletero requiere un programa que calcule el precio de sus viajes a partir de la cantidad de kilómetros que recorre. Para eso cuenta con la siguiente tarifa:
#  · Viaje mínimo $2700. Sólo se cobra cuando el importe por kilómetro no  alcanza este mínimo.
#  · Si recorre entre 0 y 10 km: $400 por km
#  · Si recorre 10 km o más: $200 por km

'''# km=float(input("ingrese la cantidad de km recorridos "))
# tarifa_minima=2700
# if km>=10:
#     km=km*200
#     print("El precio es $",km)
# elif 1<km<10:
#     km=km*400
#     print("El precio es de $",km)
# else:
#     print("Se cobra la tarifa minima de $",tarifa_minima)'''




# Ejercicio 8: Leer un número correspondiente a un año e imprimir un mensaje indicando si es bisiesto o no. 
# Un año es bisiesto cuando es divisible por 4.
#  Sin embargo, aquellos  años que sean divisibles por 4 y también por 100 no son bisiestos, a menos que  también sean divisibles por 400. Por ejemplo, 1900 no fue bisiesto pero sí el  2000.
'''
año=int(input("Ingrese el año a consultar bistuosidad "))
if año%4==0 and año%100==0 and año%400==0:
    print("El año es bisiesto 3")
elif año%4==0 and año%100==0:
    print("El año no es bisiesto 2")
elif año%4==0:
    print("El año es bisiesto 1")
else:
    print("El año no es bisiesto 4")
'''