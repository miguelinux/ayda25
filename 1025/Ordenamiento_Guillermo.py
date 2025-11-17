#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
"""
Algoritmo de Ordenamiento FULANO
"""
import random
import time
import os

from bubble_sort import ordenar as bubble_sort
from bucket_sort import ordenar as bucket_sort
from heapsort import ordenar as heap_sort
from insertion_sort import sort as insertion_sort
from merge_sort import ordenar as merge_sort
from quick_sort import sort as quick_sort
from seleccionshort import ordenar as selection_sort

# 100, 1_000, 10_000, 100_000, 1_000_000
cantidad_de_elementos = 100_000
inicio = 0
fin = cantidad_de_elementos

nombre_de_archivo_de_tiempos = "Tarea_Guillermo_Eliseo_Guzman_Lopez.csv"

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
    duracion_qs = obtener_tiempo("bubble_sort", bubble_sort, lista)
    duracion_ms = obtener_tiempo("bucket_sort", bucket_sort, lista)
    duracion_ss = obtener_tiempo("heapsort", heap_sort, lista)
    duracion_qs = obtener_tiempo("insertion_sort", insertion_sort, lista)
    duracion_ms = obtener_tiempo("merge_sort", merge_sort, lista)
    duracion_ss = obtener_tiempo("quick_sort", quick_sort, lista)
    duracion_ss = obtener_tiempo("seleccionshort", selection_sort, lista)
    
   
    es_nuevo = True
    if os.path.exists(nombre_de_archivo_de_tiempos):
            es_nuevo = False
    with open(nombre_de_archivo_de_tiempos,"a", encoding="utf-8") as archivo:
        if es_nuevo:
            archivo.write("Algoritmo,Cantidad de elementos,Tiempo\n")
            archivo.write(f"Bubble sort,{cantidad_de_elementos:_},{duracion_qs:_}\n")
            archivo.write(f"Bucket sort,{cantidad_de_elementos:_},{duracion_ms:_}\n")
            archivo.write(f"Heapsort,{cantidad_de_elementos:_},{duracion_ss:_}\n")
            archivo.write(f"Insertion sort,{cantidad_de_elementos:_},{duracion_qs:_}\n")
            archivo.write(f"Merge sort,{cantidad_de_elementos:_},{duracion_ms:_}\n")
            archivo.write(f"Quick sort,{cantidad_de_elementos:_},{duracion_ss:_}\n")
            archivo.write(f"Seleccionshort,{cantidad_de_elementos:_},{duracion_ss:_}\n")
        else:
            archivo.write("Algoritmo,Cantidad de elementos,Tiempo\n")
            archivo.write(f"Bubble sort,{cantidad_de_elementos:_},{duracion_qs:_}\n")
            archivo.write(f"Bucket sort,{cantidad_de_elementos:_},{duracion_ms:_}\n")
            archivo.write(f"Heapsort,{cantidad_de_elementos:_},{duracion_ss:_}\n")
            archivo.write(f"Insertion sort,{cantidad_de_elementos:_},{duracion_qs:_}\n")
            archivo.write(f"Merge sort,{cantidad_de_elementos:_},{duracion_ms:_}\n")
            archivo.write(f"Quick sort,{cantidad_de_elementos:_},{duracion_ss:_}\n")
            archivo.write(f"Seleccionshort,{cantidad_de_elementos:_},{duracion_ss:_}\n")

if __name__ == "__main__":
    main()
