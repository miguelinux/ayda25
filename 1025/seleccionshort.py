#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
"""
Algoritmo de Ordenamiento por Selección (Selection Sort)
"""
import random
import time

cantidad_de_elementos = 100
inicio = 0
fin = 100


def ordenar(arr):
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
    lista = [random.randint(inicio,fin) for _ in range(cantidad_de_elementos) ]
    ordenada = lista.copy()

    #tiempo_inicio = time.time()
    #ordenar_seleccion(ordenada)
    #tiempo_fin = time.time()
    tiempo_inicio_ns = time.perf_counter_ns()
    ordenar(ordenada)
    tiempo_fin_ns = time.perf_counter_ns()

    duracion_us = (tiempo_fin_ns - tiempo_inicio_ns) / 1000  # Convirtiendo de ns a us
    #print(f"La función se ejecutó en: {duracion:.6f} segundos.")
    print(f"La función se ejecutó en: {duracion_us:.3f} microsegundos.")
    print("Lista desordenada", lista)
    print("Lista ordenada", ordenada)
if __name__ == "__main__":
    main()

