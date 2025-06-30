'''print("hola mundo")

usuario=input("Indique su nombre de usuario ")
print("hola",usuario)'''

#Calculo de diferencia y suma de numeros
'''num1=int(input("indique primer numero "))
num2=int(input("indique segundo numero "))
suma=num1+num2
resta=num2-num1
print("La suma de los numeros es ",suma,"y la diferencia de los numeros es ",resta)'''

#Ingresar 3 numeros y mostrar la suma y el promedio
'''num1=int(input("ingrese el primer numero "))
num2=int(input("ingrese el segundo numero "))
num3=int(input("ingrese el tercer numero "))
suma=num1+num2+num3
promedio=suma/3
print("La suma de los numeros ingresados es de ",suma, " y el promedio es de ",promedio)'''

#EJERCICIO1 E.
#ingresar el monto de la factura y calcular iva
'''factura=int(input("Ingrese el monto de la factura "))
iva=factura*0.21
print("el IVA es de $",iva)'''

#EJERCICIO3
#Calcular el promedio de las notas qie pbtiene un alumno al rendir 2 parciales
'''primerParcial=int(input("ingrese su nota del primer parcial "))
segundoParcial=int(input("ingrese su nota del segundo parcial "))
promedio=(primerParcial+segundoParcial)/2
print("Su promedio es de ",promedio)
'''

#EJERCICIO4
#tres personas invierten dinero para fundar una empresa(no necesariamente tiene que ser partes iguales)Calcular que porcentaje invirtio cada uno
'''primerinversion=int(input("ingrese el monto a invertir del primero "))
segundoinversion=int(input("ingrese el monto a invertir del segundo "))
tercerinversion=int(input("ingrese el monto a invertir del tercero "))
inversiontotal=primerinversion+segundoinversion+tercerinversion
promedio=inversiontotal/3
porcentaje1=(primerinversion/inversiontotal)*100
porcentaje2=(segundoinversion/inversiontotal)*100
porcentaje3=(tercerinversion/inversiontotal)*100
print("la inversion total es de ",inversiontotal,"esta repartida en %",porcentaje1,", %",porcentaje2,", %",porcentaje3)'''

#EJERCICIO5
#Una persona quiere invertir su capital en un banco y quiere saber ciento dinero gana en un mes si el banco paga 2% ensual¿Cuanto ganará en seis meses si deja su dinero invertido?
'''
capital=int(input("ingrese el monto a inverir: "))
#formato simple
'''
'''
interes=capital+capital*0.02*6

#formato con intento de for

interes=capital+capital*0.02
interes1=interes+interes*0.02
interes2=interes1+interes1*0.02
interes3=interes2+interes2*0.02
interes4=interes3+interes3*0.02
interes5=interes4+interes4*0.02

print("El interes generado por el banco en el lapso de 6 meses es de: ",interes5)'''

#EJERCICIO 6
#Leer una medida en metros e imprimir esta medida expresada en centimetros, pulgadas, pies y yardas. Los factores de conversion son:1 pie=12 pulgadas-1 yarda= 3 pies- 1 pulgada=2.54cm - 1metro= 100cm
'''
medidaOriginal=int(input("ingrese la medida (en metros) a modificar: "))

cm=medidaOriginal*100
pulgada=cm/2.54
pie=pulgada/12
yarda=pie/3

print("El equivalente de medidas es:\nCM:",cm,"\npulgada:", pulgada,"\npie", pie,"\nyarda", yarda)
'''

#EJERICICO 7
#Una inmobiliaria paga a sus vendedores un salario base, más una comision fija por cada venta realizada, mas el 5% del valor de esas ventas. Realizar un programa que imprima el numero de vendedor y el salario que le corresponde en un determinado mes. Se leen por el teclado el numero de vendedor, la cantidad de ventas que realizó y el valor total de las mismas.
'''
vendedor=input("Introduce el numero de vendedor: ")
numeroDeVentas=int(input("Introduce la cantidad de ventas realizadas: "))
valorDeVentas=int(input("Ingrese el valor total de las ventas: "))
salarioBase=100000
salarioFinal=salarioBase+numeroDeVentas*10000+valorDeVentas*0.05
print("El vendedor",vendedor,"realizo",numeroDeVentas,"ventas y su salario es de 155$",salarioFinal)'''

#EJERCICIO 8 
#Un banco necesita para sus cajeros de la sucursal un programa que lea la cantidad de dinero que desesa retirar el cliente e imprima a cuantos billetes equivale, considereando que existen billetes de $1000, $500, $200, $100, $50, $20 y el resto en monedas de $10, $5, $2, $1. Desarrollar dicho programa de tal forma que se minimice la cantidad de billetes entregados por el cajero
'''
monto=int(input("Ingresar la cantidad a retirar: "))
miles=int(monto/1000)
quinientos=int((monto - miles*1000)/500)
docientos=int((monto-miles*1000-quinientos*500)/200)
print("Retirá:\n miles:",miles,"\n quinientos:",quinientos,"\ndocientos:",docientos)'''





#Ejercicio 9
#Leer un periodo en segundos e imprimirlo expresado en dias, horas, minutos y segundos. Por ejemplo, 200000 segundos equivalen a 2 dias, 7 horas, 33 minutps y 20 segundos.

'''segundos=int(input("ingrese una cantidad de segundos"))'''



#Parte 4: estructura iterativa

#1 escribir un algoritmo que muestre los primeros 25 numeros naturales

'''for i in range (1,26):
    print(i)'''




#2Calcular e imprimir la suma de los numeros comprendidos entre 42 y 176

'''suma=0

for numero in range (42,177):
    print(suma)
    suma=suma+numero'''

#3 Mostrar las tablas de multiplicar (entre 1 y 10) del numero 4 ¿Como cambiara el algoritmo para que el usuario pueda decidir la tabla de multliplicar a mostrar??

'''numero=int(input("ingrese el numero que quiera calcular la tabla")) 

for i in range (1,11):
    resultado=numero*i
    print(numero,"x",i,"=",resultado)'''


4# Leer 10 numeros enteros e imprimir el promedio, el mayor y en que orden fue ingresado el mayor valor, si se ingreso mas de una vez debe informar el primer ingreso

# numero=int(input("ingrese 10 numeros "))
'''promedio=0
mayor=0
orden=0
i=1

for i in range(10):
    numero=int(input("ingrese un numero "+ str(i)))
    promedio=promedio+numero
promedio=promedio/10
print("el promedio es de ",promedio)'''



'''numero=int(input("ingrese el numero 1:"))
suma=numero
mayor=numero
orden_mayor=1
i=2

while i<=10:
    numero= int(input("ingrese el numero " + str(i)+":"))
    suma=suma+numero
    if numero>mayor:
        mayor=numero
        orden_mayor=i
    i=i + 1
promedio=suma/10

print("promedio: ",promedio)
print("mayor valor ingresado ",mayor)
print("el mayor valor fue ingresado en el orden ",orden_mayor)'''


#5 Escribir un algoritmo que lea numeros enteros hasta que se ingrese un 0, y muestre el maximo, el minimo y la media de todos. Piense como debe inicializar las variables.

'''suma=0
sumador=0

numero=int(input("ingrese un numero para comenzar y 0 para finalizar "))
if numero!=0:
    maximo=numero
    minimo=numero        
    while numero != 0:
        suma=suma+numero
        numero=int(input("ingrese otro numero para comenzar y 0 para finalizar "))
        if numero<minimo and numero>=1:
            minimo=numero
        if numero>maximo:
            maximo=numero
        sumador+=1
    promedio=suma/sumador
    print("El promedio es de ",promedio)
    print("El maximo es: ",maximo)
    print("El minimo es: ",minimo)

else:
    print("ingresasto un numero invalido")'''


#6 Ingresar numeros, hasta que la suma de los numeros pares supere 100.Mostrar cuantos numeros en total se ingresaron.

'''numero=int(input("ingrese un numero menor o igual a 100 para empezar: "))
es_par=numero%2
sumador=numero
contador=1

while sumador<=100:

    if es_par==0:
        numero=int(input("ingrese otro numero: "))
        sumador+=numero
        contador+=1
    else:
        numero=int(input("ingrese otro numero: "))
        contador+=1
else:
    print("La suma de tus numeros pares llegaron a 100 y cantidad de numeros ingresados son",contador)'''
#aca lo hice bien, corta cuando llegas a 100 sumando solo los pares
'''if numero<=100 and espar==0:
    contador=1
    sumador=numero
    while sumador<=100 and espar==0:
        numero=int(input("ingrese otro numero "))
        contador+=1
        sumador+=numero
        espar=numero%2
    else:
            print("el numero es mayor a 100 o no es par")
    print("La cantidad de numeros ingresados fue ",contador)
else:
    print("el numero es mayor a 100 o no es par")'''
#aca lo hice mal, corta cada vez que ingresas un numero impar




#7 Un negocio desea saber el importe total recaudado al final del dia, desea contar con un preograma que que pueda ingresar el importe de cada venta realizada. Para indicar que finalizo el dia se ingresa -1 ¿Cual fue el monto total vendido y cuantas ventas se realizaron? El importe de cada venta realizada debe ser un valor positivo.


'''venta=float(input("Ingrese el valor de la venta(-1 para finaliar el dia)"))
sumador=0
contador=0

if venta>=-1:
    while venta !=-1:  
        sumador+=venta
        contador+=1
        venta=float(input("Ingrese el valor de la venta(-1 para finaliar el dia)"))
    else:
        print("Se vendió: $",sumador,)
        print("Se realizaron",contador,"ventas")
    
else:
    print("La venta tiene que ser positiva")'''




#8 Se desea analizar cuantos autos circulan con patente que tiene numeracion par y cuantos con numeracion impar en el dia. Le solicitan escribir un algoritmo que permita ingresar la terminacion de la patente(entre 0 y 9) hasta ingresar -1 e informar cuantas se inresaron con numeracion par y cuantas con numeracion impar

'''patente=int(input("ingresar la terminacion de la patente(entre 0 y 9) hasta ingresar -1: "))
par=0
inpar=0
while patente !=-1:
    es_par=patente%2
    if es_par==0:
        par+=1
    else:
        inpar+=1
    patente=int(input("ingresar la terminacion de la patente(entre 0 y 9) hasta ingresar -1: "))

else:
    print("Las patentes impar fueron: ",inpar)
    print("Las patentes pares fueron: ",par)'''




#9 leer los numeros a y b(enteros positivos).calcular el producto A*B por sumas sucesivas e imprimir el resultado. Ejemplo 4^3=4+4+4(4 multiplicado 3 veces).

'''A=int(input("ingrese la base: "))
B=int(input("Ingrese el exponente: "))
exponente=0

for i in range(B):
    exponente=exponente+A

print("El resultado es: ", exponente)'''



#10 leer los numeros naturales A y B. Calcular a sobre B por productos sucesuvos y mostrar el resultado. Ejemplo: 4*3=4*4*4*

'''A=int(input("ingrese la base: "))
B=int(input("Ingrese el exponente: "))
exponente=1

for i in range(B):
    exponente=exponente*A
    
    print(i)

print("El resultado es: ",exponente)'''

#11 Cada cliente que va al banco express, indica su nuero de documentos y aguarda a ser atendiddo, cuando finaliza la atencion del dia se ingresa -1 para indicar que no hay mas clientes para ser atendidos. El banco desea saber quien fue el primer cliente atendido y quien fue el ultimo.

'''cliente=0
contador=0
primero=0
ultimo=0

while cliente!=-1:
    cliente=int(input("Ingrese el numero de documento del cliente y espere a ser atendido: "))
    if cliente!=-1:
        if cliente>0:
            contador+=1
            if contador==1:
                primero=cliente
            else:
                ultimo=cliente
        else:
            print("El domuento debe ser positivo")
else:
    print("La cantidad de clientes fue ",contador)
    print("El primer cliente fue ",primero,"y el ultimo fue ",ultimo)'''




#12 Ingresar un numero n, validar que sea positivo. Luego: mostrar los n numeros impares hasta el numero ingresado e informar la sumas de esos numeros impares.

'''n=0
n_impar=0
respuesta=""
sumador=0

n=int(input("ingresar un numero positivo y se le devolvera los impares anteriores "))
if n>1:
    for i in range(n):
        if n_impar%2!=0:
            sumador+=n_impar
            respuesta+=str(n_impar)+ " "
        n_impar+=1
    print("los impares son ",respuesta,"y la suma es ",sumador)
else:
    print("Debe ser un numero positivo ")'''


#ejercicios integradores

#1 leer los numeros que representan edades de un grupo de personas, finalizando la lectura cuando se ingrese el numero 999. Imprimir cuantos son menores de 18 años, cuantos tienen 18 años o mas y el promedio de edad de ambos grupos. Descartar valores que no representen una edad valida.(se considera valido una edad entre 0 y 100)

'''mayores=0
suma_edades_may=0

menores=0
suma_edades_men=0

edad=0

while edad!=999:
    edad=int(input("ingrese la edad de la persona"))
    if 0<edad<100:
        if edad>=18:
            suma_edades_may+=edad
            mayores+=1
        else:
            suma_edades_men+=edad
            menores+=1
    else:
        print("la edad debe ser entre 1 y 99")
promedio_mayores=suma_edades_may/mayores
promedio_menores=suma_edades_men/menores
print("Los mayores son ",mayores,"y el promedio es",promedio_mayores)

print("Los menores son ",menores,"y el promedio es ",promedio_menores)'''


#2 Escribir un algoritmo que permita ingresar los numeros de legajo de los alumnos de un curso y su nota de examen final. El fin de la carga se determina ingresando un -1 en el legajo. informar para cada alumno si aprobo o no el examen considerando que se aprueba con nota mayor o igual a 4. se debe validar que la nota ingresada sea entre 1 y 10. terminada la carga de datos, informar:
#cantidad de alumnos que aprobaron con nota mayor o igual a 6
#cantidad de alumnos que desaprobaron el examen. Nota menor a 4
#procentaje de alumnos que estan aplazados(tienen 1 en el examen)

'''aprobados=0
desaprobados=0
aplazados=0

n_legajo=0

while n_legajo!=-1:
    n_legajo=int(input("ingrese el numero de legajo "))
    if n_legajo!=-1:
        nota=float(input("ingrese la nota sacada "))
        if nota>0 and nota<=10:
            if nota>=4:
                aprobados+=1
            elif 1<nota<4:
                desaprobados+=1
            else:
                aplazados+=1
        else:
            print("Ingrese una nota valida")
else:
    print(" Los aprobados son: ",aprobados,"\n Los desaprobados fueron: ",desaprobados,"\n Los aplazados fueron: ",aplazados)'''


#3 Una empresa aplica el siguiente procedimiento en la comerzializacion de sis productos:
    #Aplica el precio base a la primera docena de unidades
    #Aplica un 10% de descuento a todas las unidades entre 13 y 100
    #aplica un 25% de descuento a todas las unidades por encima de las 100

#Escribir un algoritmo que lea la cintidad solicitada de un producto y su precio base, y muestre el valor total de la venta y el precio promedio por unidad. El fin de carga se determina ingresando -1 como cantidad solicitada.
    #Al finalizar:
    #Canidad de ventas realizadas total
    #cantidad de ventas que se aplicaron un 10% de descuento.
    #Cantidad de ventas que solo se aplico el precio base, no se le realizaaron descuentos

'''vtas=0           #acumulador de ventas totales
vtas25=0
vtas10=0
vtas0=0
unidades=0
precio=0         #precio base
valor=0          #acumulador del valor total de la venta. La tuve que comentar para que no se acumulen los resultados de las ventas


while unidades!=-1:
    unidades=int(input("ingrese la cantidad de entradas "))
    if unidades!=-1:
        vtas+=unidades
        c_vtas=unidades
        precio=int(input("ingrese el valor base "))
        if unidades>100:  #me fijo si es mayor a 100
            unidades100=unidades  #muevo datos
            unidades100-=100  #selecciono la cantidad de entradas > 100
            unidades-=unidades100  #a las entradas les resto las q ya seleccioné
            vtas25+=unidades100                                    #sumo la cantidad de ventas total con 25 de descuento 
            valor+=unidades100*(precio*0.75)                       #sumo el precio al valor total de la venta
        if 12<unidades<=100:  
            unidades10=unidades                                   
            unidades10-=12
            unidades-=unidades10                                       
            vtas10+=unidades10                                    
            valor+=unidades10*(precio*0.90) 
        if 0<unidades<=12:                                                                             
            vtas0+=unidades                                    
            valor+=unidades*precio
        promedio=valor/c_vtas
        print("El valor total de la venta fue de ",valor,"\nEl precio promedio de las entradas es de ",promedio)
        valor=0
print("Total de ventas: ",vtas,"\nVentas con 10% de descuento:",vtas10,"\nVentas sin descuentos: ",vtas0)'''


#4 Una empresa factura a sus clientes el ultimo dia de cada mes. Si el cliente paga si factura dentro de los primeros 10 dias del mes siguiente, tiene un descuento de $120 o del 2% de la factura, lo qie resulte mas conveniente para el cliente. Si paga en los siguientes 10 dias del mes debera pagar el importe original de la factura , mientras que si paga despues del dia 20 debera abonar una multa de 150 o del 10% de su factur, y emita un informe donde conste el numero del cliente y los 3 importes que podra abonar segun la fecha de pago


'''nro_cte=0
importe=0
importe1=0
importe2=0
fecha=0

nro_cte=int(input("ingrese el numero de cliente "))
importe=int(input("ingrese el importe original "))
fecha=int(input("ingrese el dia del mes que realiza el pago "))
dto1=importe/100*2
multa=importe/100*10

#if 1<=fecha<=10:
if dto1>120:
    importe1=importe-dto1
importe1=importe-120
#if 20<fecha<=31:
if multa<150:
    importe2=importe+multa
importe2=importe+150

print("Nro de cliente: ",nro_cte,"\nimporte a pagar entre 1 y 10: ",importe1,"\nimporte a pagar entre el 11 y 20: ",importe,"\nimporte a pagar despues del 20: ",importe2)'''


#5 El factorial de un numero entero N mayor que cero se define como el producto de todos los enteros x tales que 0 < x <= N. Desarrollar un programa para calcular el factorial de un numero dado hasta ingresar -1. Deberan rechazarce las entradas invalidas (menores a 0). Al finalizar informar cuantas veces se calculo el factorial

'''numero=0
factorial=1
contador=1
cantidad_fact=0

while numero !=-1:
    numero=int(input("ingrese el numero a factorizar "))
    if numero>0:
        for contador in range(numero):
            factorial+=contador*factorial
            print(factorial)
        cantidad_fact+=1
    factorial=1

print("La cantidad de fatoriales fueron: ",cantidad_fact)'''

#6 Leer tres numeros D, M y A correspondientes al dia, mes y año de una fecha, y un numero entero N que representa una cantidad de dias. Realizar un programa que imprima la nueva fecha que resulta de sumar N dias a la fecha dada. Tener en cuenta los años bisiestos tal como se detalla en el ejercicio 9 de la practica 3

'''D=int(input("ingresa el dia de la fecha :"))
M=int(input("ingresa el mes de la fecha :"))
A=int(input("ingresa el año de la fecha :"))
N=int(input("ingresa el numero a correr :"))

Fecha1=D,"/",M,"/",A


if 1<=D<=31 and 1<=M<=12 and A>=0 and N>0:
    D+=N
    if D>30:
        M+=1
        D-=N
        N=D-30
        if N<0:
            N=N*-1
        D=N
    if M>12:
        A+=1
        D=1
        M=1
Fecha2=D,"/",M,"/",A
print("la fecha era: ",Fecha1," y se quieren pasar",N,"dias\nPor lo tanto la nueva fecha es: ",Fecha2)'''


#Una empresa cuenta con N empleados, divididos en tres categorias A,B y C. Por cada empleado se lee su legajo, categoria y salario. Se solicita elaborar un informe que contenga:
#importe total de salarios pagados por la empresa.
#Cantidad de empleados que ganan mas de $20000
#cantidad de empleados que ganan menos de $5000, cuya categoria sea C
#Legajo del empleado que mas gana
#Sueldo mas bajo
#Importe total de sueldos por cada categoria
#Salario promedio


'''N=int(input("ingrese la cantidad de empleados: "))
bien_pagos=0
mal_pagos=0
mejor_sueldo=0
legajo_mejor_sueldo=0
peor_sueldo=False
sueldosA=0
sueldosB=0
sueldosC=0
salarios=0
salario_promedio=0
categoria=0



for i in range (N):
    empleado=int(input("Ingrese el legajo del empleado: "))
    categoria=input("Ingrese la categoria(A=1_B=2_C=3): ")
    salario=float(input("ingrese el salario pagado al empleado: "))
    if salario>mejor_sueldo:
        mejor_sueldo=salario
        legajo_mejor_sueldo=empleado
    if salario<peor_sueldo:
        peor_sueldo=salario
    if salario>20000:
        bien_pagos+=1
    if salario<5000 and categoria==2:
        mal_pagos+=1
    if categoria==1:
        sueldosA+=salario
    elif categoria==2:
        sueldosB+=salario
    elif categoria==3:
        sueldosC+=salario
    salarios+=salario
    
salario_promedio=salarios/N
print("los salarios fueron: ",N)
print("El importe total de salarios fue: ",salarios)
print("Cantidad de empleados que ganan mas de $20000: ",bien_pagos)
print("cantidad de empleados que ganan menos de $5000, cuya categoria sea C",mal_pagos)
print("Legajo del empleado que mas gana: ",legajo_mejor_sueldo)
print("Sueldo mas bajo: ",peor_sueldo)
print("Importe total de sueldos por cada categoria A: ",sueldosA,"categria B: ",sueldosB,"Categoria C: ",sueldosC)
print("Salario promedio: ",salario_promedio)'''



#8 ingresar por teclado la cantidad de terminos a generar de la siguiente serie:

#1 7 19 43 91 187 379 763 1531 3067 6139
#El primer termino es el 1 y cada termino se genera como el doble del termino anterior mas 5. Mostrar la serie por pantalla e informar la suma de lso terminos generados

'''f0=2
f1=1
f3=0

n=int(input("ingrese un numero"))
if n>=1:
    for i in range(n):
        f3=f0
        f0=f0+f1
        f1=f3
        print(f0)'''




#punto 2 del parcial(secuencia de fibonacci)
'''f0=0
f1=1
f3=0
n=int(input("ingrese los numeros"))
if n>=1:
    for i in range(n):
        print(f0)
        f3=f0
        f0=f0+f1
        f1=f3
else:
    print("el numero debe ser mayor o igual a 1")'''




#---------------------------Sub-Algoritmos------------------------------------------------------




#1 Diseñar una funcion que reciba dos parametros numericos  de la multiplicacion de ambos utilizando solo sumas. Desarrollar un programa principal para crear la siguiente serie numerica de n terminos, comienza en uno y cada siguiente termino se obtiene multiplicando el anterior por la ubicacion.
#Ejemplo: 1,2,6,24,120,720,5040,40320,362880,3628800

'''def parametros(a,b):
    a=int(input("ingrese el primer numero"))
    b=int(input("ingrese el segundo numero"))
    return a,b

def multiplicar(a,b):
    resultado=0
    for i in range(b):
        resultado+=a
    return resultado


resultado=0
a,b=parametros()
print(parametros(a,b))
print(multiplicar(a,b))'''




#diseñar una funcion que multiplique dos numeros
'''def multiplicacion(a,b):
    resultado=0
    for i in range(b):
        resultado+=a
    return resultado


a=int(input("ingrese el primer numero: "))
b=int(input("ingrese el segundo numero: "))
print(multiplicacion(a,b))'''




#Armar una funcion que multiplique el numero recursivo


'''i=1
num=1
n=int(input("ingrese la cantidad de terminos a generar: "))
for i in range(n):
    num*=i+1
    print(num)'''


#2  Diseñar una funcion que reciba dos numeros enteros como parametros enteros A y B, y permita obtener A´B mediante multiplicaciones sucesivas. Desarrollar un programa prncipal para generar N veces dos valores al azar en un rango desde hasta ingresado por teclado y calcular A´b, mostrar por pantalla los valores creados y el resultado de la operacion.

'''def exponente(A,B):
    # c=A
    # for i in range (B):   no te compliques tanto, hay operadores de exponenciales
    #     A**B
    A**=B
    return(A) 



A=int(input("ingrese el valor de la base: "))
B=int(input("ingrese el valor del exponente: "))
print(exponente(A,B))'''



#3 Diseñar una funcion para mostrar un titulo filas de asteriscos, la longitud de la fila de asteriscos y el texto del titulo se recibe como parametro. Ejemplo: titulo"ejercicio3",15 muestra:
#***************
#ejercicio 3
#***************
#desrrollar un programa principal para mostrar el titulo:"Aprendiendo funciones", del ejercicio 4 al 8 agregar un titulo al iniciar el programa relacionado a lo que va a resolver el problema.

'''def subrallado(num):
    asteriscos=""
    for i in range (num):
        asteriscos+="*"
    return asteriscos


def portada(titulo,asteriscos):
    print(asteriscos)
    print(titulo)
    print(asteriscos)


titulo=str(input("ingrese el titulo del trabajo: "))
num=int(input("ingrese longitud del subrrallado: "))
asteriscos=subrallado(num)
portada(titulo,asteriscos)
'''



#4  Desarrollar dos funciones
# 1) Función para sumar los dígitos de un número. Recibe un número y retorna la suma de los dígitos. (NO utilizar cadenas de caracteres str, para lograr el objetivo)

# 2) Extraer un dígito de un número. La función recibe como parámetros dos números enteros, uno será del que se extraiga el dígito y el otro indica qué cifra se desea obtener. La cifra de la derecha se considera la número 0. Retornar el valor -1 si no existe el dígito solicitado. Tener en cuenta que el número puede ser positivo o negativo. Ejemplo: extraerdigito(12345, 1) devuelve 4, y extraerdigito(12345, 8) devuelve -1.
# Desarrollar un programa para generar valores al azar de 5 dígitos hasta que el dígito central sea cero.
# Mostrar por pantalla este número y la suma de sus dígitos utilizando ambas funciones creadas y no olvidar mostrar un título al inicio utilizando la función del ejercicio 3

#1)

'''def sumaDeDigitos(num):
    resultado=0
    while num>0:
        resultado+=num%10
        num//=10
    return(resultado)
resultado=0
num=int(input("ingrese un numero: "))
print(sumaDeDigitos(num))'''

#2)

'''def extraerPosicion(numero,cifra):
    numero = str(numero)
    cifra = str(cifra)
    largo=len(numero)
    retorno=-1
    for i in range (largo):
        if numero[i] == cifra:
            retorno=i
    return(retorno)

numero=(input("ingrese el numero a examinar: "))
cifra=(input("ingrese el numero que quiere xonfirmar que esta dentro del anterior: "))

print(extraerPosicion(numero,cifra))'''

#Funcion de generar un numero random

'''import random

def generarNumeroAzar():
    num=str(random.randint(0, 99999)) 
    while num[2]!= "0":
        num= str(random.randint(0,99999))
    return int(num)'''

#uso del retorno de una variable para usarla en otra

'''
print(generarNumeroAzar())
num=generarNumeroAzar()
print(sumaDeDigitos(num))'''

#7  Desarrollar dos funciones:
#1) Diseñar una función que solicite por teclado un número y lo retorne solo si el número ingresado es natural, caso contrario la función deberá seguir solicitando el número. 
#2) Función para sumar los primeros N números naturales de un valor. Retorna la suma. Desarrollar un programa principal para ingresar una cantidad de valores naturales (la cantidad se solicita al usuario). Para cada valor informar la suma de los primeros

'''#1)
def solicitarNatural():
    numero=-1
    while numero<0 or numero%1!=0:
        numero=float(input("ingrese un numero natural(en caso contrario se volvera a repetir la solicitud)"))
    else:
        return int(numero)

print (solicitarNatural())'''

'''#2)

def sumaDeNDigitos():
    numero=input("ingrese el numero a calcular")
    digitos=int(input("ingrese cuantos digitos quiere sumar(d¿se inicia a sumar desde la primer posicion)"))
    suma=0
    while digitos>len(numero):
        digitos=int(input("la cantidad de digitos a calcular no corresponde con la cantidad del numero.Por favor ingresar otra cantidad de digitos"))
    else:
        for i in range(digitos):
            suma+=int(numero[i])
            print(numero[i])
    return(suma)

print("La suma de los numeros seleccionados es: ",sumaDeNDigitos())'''



# 7: Estructuras de datos listas o arreglos

#1 Escribir una función que solicite ingresar una serie de números entre a y b y guardarlos en una lista. En caso de ingresar un valor fuera de rango el programa mostrará un mensaje de error y solicitará un nuevo número. Para finalizar la carga se deberá ingresar -1. La función no recibe ningún parámetro, y devuelve la lista cargada (o vacía, si el usuario no ingresó nada) como valor de retorno.

'''def crearLista(): 
    a=int(input("ingrese el limite minimo: "))
    b=int(input("ingrese el limite maximo: "))
    while b<a:
        print("Vuelva a ingresar los valores(recordar que primero el minimo y luego el maximo)")
        a=int(input("ingrese el limite minimo: "))
        b=int(input("ingrese el limite maximo: "))
    n=0
    lista=[]
    while n!=-1:
        n=int(input("ingrese un numero: "))
        if a<n<b: #or b>n<a: a<n>b or b<n>a:
            lista.append(n)
        else:
            print("¡Debe ingresar un numero dentro de los limites!")
    return lista
print(crearLista())'''


#2  Escribir una función para crear una lista con N números al azar en un rango de valores que se recibe por parámetro. La función devuelve la lista cargada (o vacía si el rango indicado no es válido).

'''
import random

def crearListaEnRango():
    n=int(input("introduzca la longitud de la lista: "))
    limA=int(input("introduzca el limite inferior: "))
    limB=int(input("introduzca el limite superior: "))
    lista=[]
    for i in range(n):
        numerorandom=random.randint(limA,limB)
        lista.append(numerorandom)
    return lista

print(crearListaEnRango())
'''

#3: Calcular la suma de los números de una lista.
'''
lista=[1,2,3,]

def sumarElementosDeLista(lista):
    largo=len(lista)
    sumaTotal=0
    for i in range(largo):
        sumaTotal+=lista[i]
    return sumaTotal

print(sumarElementosDeLista(lista))
'''
#4: Desarrollar un algoritmo que permita crear al azar 5 números pertenecientes a la lista A y otros 5 números pertenecientes a la lista B. Crear una lista C, donde cada posición es el resultado de la suma del número en la misma posición en la lista A con el número en la misma posición en la lista B. Ejemplo: Se crea 
'''
import random
A = [] 
B = []
C = [] 

def crearListaDe5(A):
    for i in range(5):
        numAlAzar=random.randint(1,10)
        A.append(numAlAzar)
    return A
def crearListaDe5(B):
    for i in range(5):
        numAlAzar=random.randint(1,10)
        B.append(numAlAzar)
    return B

def sumarListas(A,B):
    for i in range(len(A)):
        resultadoC=A[i]+B[i]
        C.append(resultadoC)
    return C

print(crearListaDe5(A))
print(crearListaDe5(B))
print(sumarListas(A,B))
'''
#  5: Rellenar una lista con números enteros entre 0 y 100 obtenidos al azar e imprimir el valor mínimo y el lugar que ocupa. Tener en cuenta que el mínimo puede estar repetido, en cuyo caso deberán mostrarse todas las posiciones que ocupe. La carga de datos termina cuando se obtenga un 0 como número al azar, el que no deberá cargarse en la lista.
'''
import random
def crearListaDe100():
    listaDe100=[]
    contador=0
    bandera=True
    while bandera!=False:
        numRandom=random.randint(0,100)
        if numRandom==0 or contador==100:
            bandera=False
        else:
            contador+=1
            listaDe100.append(numRandom)
    print("se creo una lista de ",contador,"elementos")
    return listaDe100

def buscarMinimo(lista):

    valorMinimo=lista[0]
    ubicacionMinimo=[]

    for i in range(len(lista)):
        if lista[i]<=valorMinimo:
            valorMinimo=lista[i]

    for j in range(len(lista)):
        if valorMinimo==lista[j]:
            ubicacionMinimo.append(j)

    return valorMinimo,ubicacionMinimo

listaDe100=crearListaDe100()
print (listaDe100)
print (buscarMinimo(listaDe100))
'''

# 6: Determinar si una lista es capicúa

'''def listaCapicua(lista):
    mensaje = "La lista es capicua"
    for i in range(len(lista) // 2):
        if lista[i] != lista[-(i + 1)]:
            mensaje = "La lista no es capicua"

    return lista, mensaje

# Caso correcto: lista de dígitos
lista = [1, 2, 3, 5, 3, 2, 1]
print(listaCapicua(lista))'''

#7 Una escuela necesita conocer cuántos alumnos cumplen años en cada mes del año, con el propósito de ofrecerles un agasajo especial en su día. Desarrollar un programa que lea el número de legajo y fecha de nacimiento (día, mes y año) de cada uno de los alumnos que concurren a dicha escuela. La carga finaliza con un número de legajo igual a -1. Emitir un informe donde aparezca (mes por mes) cuántos alumnos cumplen años a lo largo del año. Mostrar también una leyenda que indique cuál es el mes con mayor cantidad de cumpleaños
'''
def contarCumplesDelMes(meses,mes):
    cantidad=0
    for i in range(len(meses)):
        if meses[i]==mes:
            cantidad+=1
    return cantidad

def mesPorMes():
    cantidadPorMeses=[]
    for i in range(1,13):
        cantidadPorMeses.append(contarCumplesDelMes(meses,i))
    return cantidadPorMeses

def reporte(nombreMeses,cantidadPorMeses):
    for i in range(len(nombreMeses)):
        mes=nombreMeses[i]
        cumpleañospormes=cantidadPorMeses[i]
        print(mes,":    ",cumpleañospormes)
    print("La cantidad de chicos que cumplen años son ",cumpleañosporaño())
    print("El mes con mayor cumpleaños fue: ",mesConMasCumpleaños())

def cumpleañosporaño():
    contador=len(meses)
    return contador

def mesConMasCumpleaños():
    cantidades = mesPorMes() 
    mayor_cantidad = cantidades[0]
    indice_del_max = 0
    for i in range(1, len(cantidades)):
        if cantidades[i] > mayor_cantidad:
            mayor_cantidad = cantidades[i]
            indice_del_max = i
    return nombreMeses[indice_del_max]



legajo=0
legajos=[]
dias=[]
meses=[1,3,4,2,4,5,4,7,4,2,4]
años=[]
nombreMeses=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","nobiembre","diciembre"]

legajo=int(input("ingrese el numero de legajo: "))
while legajo!=-1:
    while legajo==0 or legajo<-1:
        legajo=int(input("ingrese el numero de legajo real: "))
    else:
        dia=int(input("ingrese el dia de nacimiento: "))
        mes=int(input("ingrese el mes de nacimiento: "))
        año=int(input("ingrese el año de nacimiento: "))
        while 1>dia>30 and 1>mes>12 and 2000>año>2015:
            print("debe ingresar bien la infomacion")
            dia=int(input("ingrese el dia de nacimiento: "))
            mes=int(input("ingrese el mes de nacimiento: "))
            año=int(input("ingrese el año de nacimiento: "))
        else:
            dias.append(dia) 
            meses.append(mes)
            años.append(año)
            legajos.append(legajo)

cumpleañospormes=mesPorMes()
reporte(nombreMeses,cumpleañospormes)
'''


#  8: Escribir una función para devolver la posición que ocupa un valor pasado como parámetro, utilizando búsqueda secuencial en una lista desordenada. La función debe devolver -1 si el elemento no seencuentra en la lista.
'''
import random

def crearLista():
    lista=[]
    for i in range(5):
        num=random.randint(1,10)
        lista.append(num)
    return lista

def ordenamientoDeLista(lista):
    ordenada=True
    while ordenada:
        ordenada=False
        for i in range(len(lista)-1):
            for j in range(i+1,len(lista)):
                if lista[i]>lista[j]:
                    aux=lista[j]
                    lista[j]=lista[i]
                    lista[i]=aux
                    ordenada=True
    return lista

def busquedaDeNumero(lista,buscado):
    posiciones=[]
    for i in range(len(lista)):
        if lista[i]==buscado:
            posiciones.append(i)
    if posiciones==[]:
        resultado="No se encuentra en la lista"
    else:
        resultado="las posiciones en las que se encuentra el numero buscado son: ",posiciones
    return print(resultado)

ListaRandom=crearLista()
print("Lista random: ",ListaRandom)
ListaOrdenada=ordenamientoDeLista(ListaRandom)
print("lista random ordenada: ",ListaOrdenada)
numeroBuscado=int(input("ingrese el numero a buscar en la lista: "))
busquedaDeNumero(ListaOrdenada,numeroBuscado)
'''
# 9: Crear tres listas y ordenarlas en forma ascendente utilizando un método para cada lista: métodos de selección, inserción y burbujeo. ¿Qué cambia para ordenar en forma descendente?
'''
import random

def crearLista():
    lista=[]
    for i in range(5):
        num=random.randint(1,10)
        lista.append(num)
    return lista

def ordenamientoBurbuja(lista):
    desordenada=True
    while desordenada:
        desordenada=False
        for i in range(len(lista)-1):
            if lista[i]>lista[i+1]:
                aux=lista[i+1]
                lista[i+1]=lista[i]
                lista[i]=aux
                desordenada=True
    return lista

def ordenamientoPorInsercion(lista):
    for i in range(1,len(lista)):           #inicializa en la segunda 
        aux=lista[i]                        #guarda el contenido en un auxiliar
        j=i                                 #copia el indice
        while j>0 and lista[j-1]>aux:       #mientras el indice sea mayor a cero y el anterior al indice sea mayor al auxiliar; 
            lista[j]= lista[j-1]            #empuja el anterior al indice hacia adelante
            j-=1                            #retrocede el indice
        lista[j]=aux                        #guarda el auxiliar en la posicion del indice
    return lista

def busquedaBinaria(lista,parametro):
    izq=0
    der=len(lista)-1
    pos=-1

    
# 10: Utilizando búsqueda binaria sobre una lista ordenada realizar la búsqueda de valores e informar si se encuentran o no en la lista, finalizar las búsquedas con -1 e informar cuantas búsquedas fueron exitosas y en cuantas no se encontró el valor buscado.

    while izq <= der and pos ==-1:
        centro=(izq + der)//2
        if lista[centro]==parametro:
            pos=centro
        elif lista[centro]< parametro:    
            izq=centro+1
        else:
            der= centro-1

    return pos

lista=crearLista()
print(lista)
print (ordenamientoPorInsercion(lista))
print (ordenamientoBurbuja(lista))
parametro=int(input("ingrese el numero a buscar dentro de la lista"))
print(busquedaBinaria(lista,parametro))
'''

# 11: Crear una lista de N números generados al azar entre 0 y 100 pero sin elementos repetidos. Validar que N sea menor o igual a 100
import random
def ordenamientoBurbuja(lista):
    desordenada=True
    while desordenada:
        desordenada=False
        for i in range(len(lista)-1):
            if lista[i]>lista[i+1]:
                aux=lista[i+1]
                lista[i+1]=lista[i]
                lista[i]=aux
                desordenada=True
    return lista

def busqueda(lista,numero):
    ingresa=True
    for i in range(len(lista)):
        if lista[i]==numero:
            ingresa=False
    return ingresa



def crearLista():
    lista=[]
    n=int(input("ingrese la longitud de la lista: "))
    for i in range(n):
        numero=random.randint(0,100)
        if busqueda(lista,numero)==True:
            lista.append(numero)
    return lista
        
print(crearLista())

lista2=[19, 73, 60, 27, 7, 24, 38, 4, 97, 17, 94, 14, 62, 35, 55, 67, 43, 11, 87, 76, 37, 40, 68, 50, 86, 72, 45, 12, 8, 33, 46, 29, 28, 81, 84, 65, 71, 21, 82, 64, 79, 80, 13, 16, 66, 74, 59, 15, 63, 39, 98, 90, 49, 99, 0, 23, 95, 25, 42, 34, 85, 44, 88, 22, 6, 75, 31, 61, 56, 83, 10, 53, 36, 51, 57, 1, 69, 30, 20, 77, 91, 18, 26, 93, 32, 52, 9, 89, 58, 5, 47, 92, 96, 48, 70, 41, 3, 78, 2, 100, 54]

print(ordenamientoBurbuja(lista2))