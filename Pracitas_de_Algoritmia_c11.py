def busquedaBinaria(lista,parametro):
    izq=0
    der=len(lista)-1
    pos=-1

    while izq <= der and pos ==-1:
        centro=(izq + der)//2
        if lista[centro]==parametro:
            pos=centro
        elif lista[centro]< parametro:    
            izq=centro+1
        else:
            der= centro-1

    return pos

lista=[1,2,3,4,5,6,3]
parametro=7
print(busquedaBinaria(lista,parametro))


'''
def buscar_valor_binario_todas_posiciones(lista_ordenada, valor):  
    posiciones = []
    izquierda = 0
    derecha = len(lista_ordenada) - 1
    while izquierda <= derecha:  # Encontrar la primera aparición del valor
        medio = (izquierda + derecha) // 2
        if lista_ordenada[medio] == valor:  # Retroceder para encontrar la primera aparición
            indice = medio
            while indice > 0 and lista_ordenada[indice - 1] == valor:
                indice -= 1            
            # Agregar todas las posiciones del valor a la lista
            while indice < len(lista_ordenada) and lista_ordenada[indice] == valor:
                posiciones.append(indice)
                indice += 1            
            return posiciones
        elif lista_ordenada[medio] < valor:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return posiciones
    # Ejemplo de uso: buscar todas las posiciones del valor 6 en la lista
lista_ordenada = [1, 2, 2, 2, 3, 4, 5, 6, 6, 6, 7, 8, 9]
valor = 6    
posiciones=buscar_valor_binario_todas_posiciones(lista_ordenada, valor)
print(posiciones)'''