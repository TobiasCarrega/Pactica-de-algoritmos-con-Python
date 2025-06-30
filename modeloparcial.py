'''#Aca hago la Inicialización de contadores y acumuladores

ventas_totales = 0 
ventas_con_descuento_10 = 0 
ventas_sin_descuento = 0 
suma_precios_promedios = 0

recaudacion_futbol = 0 
recaudacion_basquet = 0 
recaudacion_tenis = 0

cantidad = 0 
fin=False

#Aca hago el Bucle while de carga de ventas

while fin==False: 
    cantidad = int(input("Ingrese la cantidad de entradas (-1 para terminar): "))
    if cantidad == -1:
        fin=True 
    else:
        precio_base = float(input("Ingrese el precio base por entrada: ")) 
        print("Tipo de evento: 1 - Fútbol | 2 - Básquet | 3 - Tenis")
        tipo_evento = int(input("Ingrese el tipo de evento (1, 2, 3): "))
        ventas_totales += 1 # esto es un contador 
# Cálculos
if cantidad <= 12: 
    total_venta = cantidad * precio_base 
    ventas_sin_descuento += 1 
elif cantidad <= 100:
    sin_descuento = 12 * precio_base
    con_10_desc = (cantidad - 12) * (precio_base * 0.90) 
    total_venta = sin_descuento + con_10_desc 
    ventas_con_descuento_10 += 1 
else: 
    sin_descuento = 12 * precio_base
    con_10_desc = (100 - 12) * (precio_base * 0.90) 
    con_25_desc = (cantidad - 100) * (precio_base * 0.75) 
    total_venta = sin_descuento + con_10_desc + con_25_desc 
    ventas_con_descuento_10 += 1 
    precio_promedio = total_venta / cantidad
    suma_precios_promedios += precio_promedio
# Recaudación por tipo de evento

if tipo_evento == 1: 
    recaudacion_futbol += total_venta 
elif tipo_evento == 2:
    recaudacion_basquet += total_venta

elif tipo_evento == 3: 
    recaudacion_tenis += total_venta # Resultados de la venta
    print(f"\n Total de la venta: ${total_venta:,.2f}")
    print(f" Precio promedio por entrada: ${precio_promedio:,.2f}\n")

#Determinar evento con mayor recaudación

mayor_recaudacion = recaudacion_futbol 
evento_top = "Fútbol"

if recaudacion_basquet > mayor_recaudacion: 
    mayor_recaudacion = recaudacion_basquet 
    evento_top = "Básquet"

if recaudacion_tenis > mayor_recaudacion: 
    mayor_recaudacion = recaudacion_tenis 
    evento_top = "Tenis"

if mayor_recaudacion == recaudacion_futbol: 
    evento_top = "Fútbol" 
elif mayor_recaudacion == recaudacion_basquet: 
    evento_top = "Básquet" 
else: evento_top = "Tenis"

#Promedio general de los precios promedio

if ventas_totales > 0: 
    promedio_general = suma_precios_promedios / ventas_totales 
else: promedio_general = 0

#Informe final

print("\n--- Informe Final ---") 
print(f" Ventas totales realizadas: {ventas_totales}") 
print(f" Recaudación Fútbol: ${recaudacion_futbol:,.2f}") 
print(f" Recaudación Básquet: ${recaudacion_basquet:,.2f}")
print(f" Recaudación Tenis: ${recaudacion_tenis:,.2f}") 
print(f" Ventas con 10% de descuento: {ventas_con_descuento_10}") 
print(f" Ventas sin descuento (hasta 12 entradas): {ventas_sin_descuento}") 
print(f" Evento con mayor recaudación:{evento_top}") 
print(f" Promedio general de los precios promedio: ${promedio_general:,.2f}")'''




esd=12
ecd10=0