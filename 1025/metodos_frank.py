#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
"""
Algoritmo de Ordenamiento TODOS LOS QUE ESTAN EN EL REPO
"""
import random
import time
import os

#from ordering_methods_luis_daniel_sainz import ordenar as qs
from merge_sort import ordenar as ms
from seleccionshort import ordenar as ss
#from quick_sort import sort as qs
from insertion_sort import sort as iso
from heapsort import ordenar as hs


# 100, 1_000, 10_000, 100_000, 1_000_000
cantidad_de_elementos = 100_000
inicio = 0
fin = cantidad_de_elementos

nombre_de_archivo_de_tiempos = "tiempos_Frank.csv"

def verifica(lista, algoritmo="sin algoritmo"):
    mayor = -10
    for elemento in lista:
        if elemento >= mayor:
            mayor = elemento
        else:
            print("No esta ordenado con", algoritmo)
            break


def obtener_tiempo (nombre, funcion, lista):
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
    lista = [random.randint(inicio,fin) for _ in range(cantidad_de_elementos) ]
    print(f"Ordenando {cantidad_de_elementos:_} elementos")
    #duracion_qs = obtener_tiempo("Quicksort", qs, lista)
    duracion_ms = obtener_tiempo("Merge sort", ms, lista)
    duracion_ss = obtener_tiempo("Selection sort", ss, lista)
    duracion_is = obtener_tiempo("Insertion sort", iso, lista)
    duracion_hs = obtener_tiempo("Heapsort", hs, lista)
   
    es_nuevo = True
    if os.path.exists(nombre_de_archivo_de_tiempos):
            es_nuevo = False
    with open(nombre_de_archivo_de_tiempos,"a", encoding="utf-8") as archivo:
        if es_nuevo:
            archivo.write("Algoritmo,Cantidad de elementos,Tiempo\n")
            #archivo.write(f"Quicksort,{cantidad_de_elementos:_},{duracion_qs:_}\n")
            archivo.write(f"Merge sort,{cantidad_de_elementos:_},{duracion_ms:_}\n")
            archivo.write(f"Selection sort,{cantidad_de_elementos:_},{duracion_ss:_}\n")
            archivo.write(f"Insertion sort,{cantidad_de_elementos:_},{duracion_is:_}\n")
            archivo.write(f"Heapsort,{cantidad_de_elementos:_},{duracion_hs:_}\n")
        else:
            print(f"Ordenados {cantidad_de_elementos:_} elementos")
            archivo.write("Algoritmo,Cantidad de elementos,Tiempo\n")
            #archivo.write(f"Quicksort,{cantidad_de_elementos:_},{duracion_qs:_}\n")
            archivo.write(f"Merge sort,{cantidad_de_elementos:_},{duracion_ms:_}\n")
            archivo.write(f"Selection sort,{cantidad_de_elementos:_},{duracion_ss:_}\n")
            archivo.write(f"Insertion sort,{cantidad_de_elementos:_},{duracion_is:_}\n")
            archivo.write(f"Heapsort,{cantidad_de_elementos:_},{duracion_hs:_}\n")

if __name__ == "__main__":
    main()

