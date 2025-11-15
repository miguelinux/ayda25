#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
"""
Algoritmo de Ordenamiento FULANO
"""
import random
import time
import os

#from ordering_methods_luis_daniel_sainz import ordenar as qs
from merge_sort import ordenar as ms
from countingsort import ordenar as cs
from  bubble_sort import ordenar as bs
from heapsort import ordenar as hs
from seleccionshort import ordenar as ss

# 100, 1_000, 10_000, 100_000, 1_000_000
cantidad_de_elementos = 100_000
inicio = 0
fin = cantidad_de_elementos

nombre_de_archivo_de_tiempos = "tarea_Giovanna.csv"

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
    duracion_cs = obtener_tiempo("Counting sort", cs, lista)
    duracion_bs = obtener_tiempo("Bubble sort", bs, lista)
    duracion_hs = obtener_tiempo("Heapsort", hs, lista)
    duracion_ss = obtener_tiempo("Selection sort", ss, lista)

    
   
    es_nuevo = True
    if os.path.exists(nombre_de_archivo_de_tiempos):
            es_nuevo = False
    with open(nombre_de_archivo_de_tiempos,"a", encoding="utf-8") as archivo:
        if es_nuevo:
            archivo.write("Algoritmo,Cantidad de elementos,Tiempo\n")
            #archivo.write(f"Quicksort,{cantidad_de_elementos:_},{duracion_qs:_}\n")
            archivo.write(f"Merge sort,{cantidad_de_elementos:_},{duracion_ms:_}\n")
            archivo.write(f"Counting sort,{cantidad_de_elementos:_},{duracion_cs:_}\n")
            archivo.write(f"Bubble sort,{cantidad_de_elementos:_},{duracion_bs:_}\n")
            archivo.write(f"Heapsort,{cantidad_de_elementos:_},{duracion_hs:_}\n")
            archivo.write(f"Selection sort,{cantidad_de_elementos:_},{duracion_ss:_}\n")
        else:
            archivo.write("Algoritmo,Cantidad de elementos,Tiempo\n")
            #archivo.write(f"Quicksort,{cantidad_de_elementos:_},{duracion_qs:_}\n")
            archivo.write(f"Merge sort,{cantidad_de_elementos:_},{duracion_ms:_}\n")
            archivo.write(f"Counting sort,{cantidad_de_elementos:_},{duracion_cs:_}\n")
            archivo.write(f"Bubble sort,{cantidad_de_elementos:_},{duracion_bs:_}\n")
            archivo.write(f"Heapsort,{cantidad_de_elementos:_},{duracion_hs:_}\n")
            archivo.write(f"Selection sort,{cantidad_de_elementos:_},{duracion_ss:_}\n")

if __name__ == "__main__":
    main()

