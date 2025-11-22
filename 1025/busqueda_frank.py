#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
"""Algoritmo de Búsqueda Secuencial y Binaria
"""
import random

# 100, 1_000, 10_000, 100_000, 1_000_000
cantidad_de_elementos = 100
inicio = 0
fin = cantidad_de_elementos

def busqueda_secuencial(lista, valor_buscado):
    """Realiza una búsqueda secuencial en una lista."""
    for i in range(len(lista)):
        # Si encuentra el valor, devuelve su índice
        if lista[i] == valor_buscado:
            return i
    # Si el bucle termina sin encontrar el valor, devuelve -1
    return -1
   

def busqueda_binaria(lista_ordenada, valor_buscado):
    """Realiza una búsqueda binaria en una lista ordenada."""
    inicio = 0
    fin = len(lista_ordenada) - 1

    while inicio <= fin:
        # Calcula el índice central
        # Se usa // para obtener una división entera (un índice)
        mitad = (inicio + fin) // 2

        # Compara el valor del centro con el valor buscado
        if lista_ordenada[mitad] == valor_buscado:
            return mitad  # ¡Encontrado! Devuelve el índice

        elif lista_ordenada[mitad] < valor_buscado:
            # Si el valor central es menor, el valor buscado debe estar en la mitad derecha
            inicio = mitad + 1
        
        else: # lista_ordenada[mitad] > valor_buscado
            # Si el valor central es mayor, el valor buscado debe estar en la mitad izquierda
            fin = mitad - 1
    
    # Si el bucle termina, el valor no se encontró
    return -1

def main():
    lista = [random.randint(inicio,fin) for _ in range(cantidad_de_elementos) ]
    elemento_a_buscar = random.choice(lista)
    #lista.sort()  # Aseguramos que la lista esté ordenada para la búsqueda
    print(f"Buscando el elemento {elemento_a_buscar} en una lista de {cantidad_de_elementos:_} elementos")
        
    indice = busqueda_secuencial(lista, elemento_a_buscar)

    if indice != -1:
        print(f"El elemento {elemento_a_buscar} se encuentra en el índice: {indice}")
        print(f"Lista: {lista}")
    else:
        print(f"El elemento {elemento_a_buscar} no se encontró en la lista.")
        print(f"Lista: {lista}")

    lista = [random.randint(inicio,fin) for _ in range(cantidad_de_elementos) ]
    elemento_a_buscar = random.choice(lista)
    lista.sort() 
    elemento_a_buscar = random.choice(lista)
    #PARA LA BUSQUEDA BINARIA SE NECESITA UNA LISTA ORDENADA
    indice = busqueda_binaria(lista, elemento_a_buscar)
    print(f"Buscando el elemento {elemento_a_buscar} en una lista ordenada de {cantidad_de_elementos:_} elementos")
    print(f"Lista ordenada: {lista}")
    print(f"Elemento a buscar: {elemento_a_buscar}")
    if indice != -1:
        print(f"El elemento {elemento_a_buscar} se encuentra en el índice: {indice}")
    else:
        print(f"El elemento {elemento_a_buscar} no se encontró en la lista.")

   

if __name__ == "__main__":
    main()


