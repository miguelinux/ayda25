#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
"""
Algoritmo de Ordenamiento por Selección (Selection Sort)

"""
import random
import time

cantidad_de_elmentos = 100
inicio = 0
fin = 100


def ordenar_seleccion(arr):
    # Obtener la longitud de la lista
    longitud = len(arr)
    # Iterar sobre cada elemento de la lista
    for i in range(longitud):
        indice_minimo = i
        # Buscar el elemento más pequeño en el resto de la lista no ordenada
        for j in range(i + 1, longitud):
            if arr[j] < arr[indice_minimo]:
                indice_minimo = j
        # Intercambiar el elemento mínimo encontrado con el elemento actual (lista[i])
        # Esto coloca el elemento más pequeño de la sublista no ordenada en su posición correcta
        arr[i], arr[indice_minimo] = arr[indice_minimo], arr[i]

    # Retornar la lista ya ordenada
    return arr

def main():
    """
    Función principal
    """
    lista = [random.randint(inicio,fin) for _ in range(cantidad_de_elmentos) ]
    ordenada = lista.copy()

    tiempo_inicio = time.time()
    ordenar_seleccion(ordenada)
    tiempo_fin = time.time()

    duracion = tiempo_fin - tiempo_inicio
    print(f"La función se ejecutó en: {duracion:.4f} segundos.")
    print("Lista desordenada", lista)
    print("Lista ordenada", ordenada)
if __name__ == "__main__":
    main()

