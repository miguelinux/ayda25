#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
"""
Algoritmo de Ordenamiento FULANO
"""
import random
import time
import os

from quick_sort import ordenar as qs
from merge_sort import ordenar as ms
from seleccionshort import ordenar as ss
from bubble_sort import ordenar as bs
from heapsort import ordenar as hs, cantidad_de_elementos
from insertion_sort import ordenar as ins

# 100, 1_000, 10_000, 100_000, 1_000_000
#cantidad_de_elementos = 100
cantidad_de_elementos = [100, 1_000, 10_000, 100_000, 1_000_000]
inicio = 0
fin = None

nombre_de_archivo_de_tiempos = "tiempos_Emmanuel_Vera.csv"


def verifica(lista, algoritmo="sin algoritmo"):
    mayor = -10
    for elemento in lista:
        if elemento >= mayor:
            mayor = elemento
        else:
            print("No esta ordenado con", algoritmo)
            break


def obtener_tiempo(nombre, funcion, lista):
    desordenada = lista.copy()
    tiempo_inicio = time.perf_counter_ns()
    ordenada = funcion(desordenada)
    tiempo_fin = time.perf_counter_ns()
    # Micro segundos
    duracion = (tiempo_fin - tiempo_inicio) / 1000
    verifica(ordenada, nombre)
    return duracion


def main():
    """
    Función principal
    """
    for elementos in cantidad_de_elementos:
        fin = elementos
        lista = [random.randint(inicio, fin) for _ in range(elementos)]
        print(f"Ordenando {elementos:_} elementos")
        duracion_qs = obtener_tiempo("Quicksort", qs, lista)
        duracion_ms = obtener_tiempo("Merge sort", ms, lista)
        duracion_ss = obtener_tiempo("Selection sort", ss, lista)
        duracion_bs = obtener_tiempo("Bubble sort", bs, lista)
        duracion_hs = obtener_tiempo("Heap sort", hs, lista)
        duracion_ins = obtener_tiempo("Insertion sort", ins, lista)

        es_nuevo = True
        if os.path.exists(nombre_de_archivo_de_tiempos):
            es_nuevo = False
        with open(nombre_de_archivo_de_tiempos, "a", encoding="utf-8") as archivo:
            if es_nuevo:
                archivo.write("Algoritmo,Cantidad de elementos,Tiempo\n")
                archivo.write(f"Quicksort,{elementos:_},{duracion_qs:_}\n")
                archivo.write(f"Merge sort,{elementos:_},{duracion_ms:_}\n")
                archivo.write(f"Heap sort,{elementos:_},{duracion_hs:_}\n")
                archivo.write(f"Selection sort,{elementos:_},{duracion_ss:_}\n")
                archivo.write(f"Bubble sort,{elementos:_},{duracion_bs:_}\n")
                archivo.write(f"Insertion sort,{elementos:_},{duracion_ins:_}\n")
            else:
                archivo.write("Algoritmo,Cantidad de elementos,Tiempo\n")
                archivo.write(f"Quicksort,{elementos:_},{duracion_qs:_}\n")
                archivo.write(f"Merge sort,{elementos:_},{duracion_ms:_}\n")
                archivo.write(f"Heap sort,{elementos:_},{duracion_hs:_}\n")
                archivo.write(f"Selection sort,{elementos:_},{duracion_ss:_}\n")
                archivo.write(f"Bubble sort,{elementos:_},{duracion_bs:_}\n")
                archivo.write(f"Insertion sort,{elementos:_},{duracion_ins:_}\n")


if __name__ == "__main__":
    main()
