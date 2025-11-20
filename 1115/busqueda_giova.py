#!/usr/bin/env python3

"""Algoritmo de Búsqueda Secuencial y Binaria
"""
import random

# 100, 1_000, 10_000, 100_000, 1_000_000
cantidad_de_elementos = 1_000
inicio = 0
fin = cantidad_de_elementos

def busqueda_binaria(lista, objetivo):
    """
    Busca un elemento usando búsqueda binaria.
    La lista debe estar ordenada.
    Devuelve el índice si lo encuentra, de lo contrario -1.
    """
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if lista[medio] == objetivo:
            return medio
        elif objetivo < lista[medio]:
            fin = medio - 1
        else:
            inicio = medio + 1

    return -1
def busqueda_secuencial(lista, objetivo):
    """
    Busca un elemento en la lista de forma secuencial.
    Regresa el índice si lo encuentra, de lo contrario -1.
    """
    for indice in range(len(lista)):
        if lista[indice] == objetivo:
            return indice
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
    """PARA LA BUSQUEDA BINARIA SE NECESITA UNA LISTA ORDENADA"""
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
