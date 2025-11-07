#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
"""
Algoritmo de Ordenamiento Bubble Sort
"""
import random
import time

cantidad_de_elmentos = 100
inicio = 0
fin = 100

def ordenar(arr):
    """Ordena una lista usando el algoritmo Bubble Sort optimizado"""
    n = len(arr)

    for i in range(n):
        swapped = False  # Optimización: detecta si ya está ordenado

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Si no hubo intercambios, la lista ya está ordenada
        if not swapped:
            break

    return arr


def main():
    """
    Función principal
    """
    tamanios = [100, 1_000, 10_000, 100_000, 1_000_000]

    for cantidad_de_elmentos in tamanios:
        lista = [random.randint(inicio, fin) for _ in range(cantidad_de_elmentos)]
        ordenada = lista.copy()

        tiempo_inicio_ns = time.perf_counter_ns()
        ordenar(ordenada)
        tiempo_fin_ns = time.perf_counter_ns()

        duracion_us = (tiempo_fin_ns - tiempo_inicio_ns) / 1000  # Convirtiendo de ns a us
        print(f"\nCantidad de elementos: {cantidad_de_elmentos:,}")
        print(f"La función se ejecutó en: {duracion_us:.3f} microsegundos.")
        # print("Lista desordenada", lista)
        # print("Lista ordenada", ordenada)


if __name__ == "__main__":
    main()
