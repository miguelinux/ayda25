#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
"""
Algoritmo de Ordenamiento Merge Sort
"""
import random
import time
import math

cantidad_de_elmentos = 100
inicio = 0
fin = 100

def ordenar(arr:list) -> list:
    # print(f'.....Called merge_sort({arr})')

    # BASE CASE - Una lista con cero o un solo elemento esta ordenada por naturaleza
    if len(arr) == 0 or len(arr) == 1:
        return arr

    # RECURSIVE CASE - Pasar las mitades izquierda y derecha a la funcion merge_sort()
    # Redondear hacia abajo si el total de elemento en la lista no se dividen exactamente a la mitad
    i_middle = math.floor(len(arr) / 2)

    # print(f"..........Split into: arr[:{i_middle}], and, arr[{i_middle}:]")

    left = ordenar(arr[:i_middle])
    right = ordenar(arr[i_middle:])

    # BASE CASE
    # En est punto la parte derecha e izquierda deberian de estar ordenadas
    # Por lo que podemos proceder a unificarlas 'merge them' en una sola lista ordenada
    sorted_result = []
    index_left = 0
    index_right = 0
    while len(sorted_result) < cantidad_de_elmentos:
        # Append el valor mas pequeño a la lista sorted_result
        if left[index_left] < right[index_right]:
            sorted_result.append(left[index_left])
            index_left += 1
        else:
            sorted_result.append(right[index_right])
            index_right += 1

        # Si alguno de los punteros (index_left, index_right) ha alcanzado el final de la lista
        # pon el resto de la otra lista (extend) en sorted_result
        if index_left == len(left):
            sorted_result.extend(right[index_right:])
            break
        elif index_right == len(right):
            sorted_result.extend(left[index_left:])
            break

    # print(f"Las dos mitades se han unificado (merged) en: {sorted_result}")
    return sorted_result    # Se retorna una version ordenada de arr


def main():
    """
    Función principal
    """
    lista = [random.randint(inicio,fin) for _ in range(cantidad_de_elmentos) ]
    ordenada = lista.copy()

    # tiempo_inicio = time.time()
    # ordenar(ordenada)
    # tiempo_fin = time.time()
    #
    # duracion = tiempo_fin - tiempo_inicio

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