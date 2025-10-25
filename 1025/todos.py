#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
"""
Algoritmo de Ordenamiento FULANO
"""
import random
import time

from quicksort import ordenar as qs
from merge_sort import ordenar as ms

cantidad_de_elementos = 100
inicio = 0
fin = 100

def verifica(lista, algoritmo="sin algoritmo"):
    mayor = -10;
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

    duracion_qs = obtener_tiempo("Quicksort", qs, lista)
    duracion_ms = obtener_tiempo("Merge sort", ms, lista)

    with open("tiempos.csv","w", encoding="utf-8") as archivo:
        archivo.write("Algoritmo,Cantidad de elementos,Tiempo,Inicio,Fin\n")
        archivo.write(f"Quicksort,{cantidad_de_elementos:.4f},{duracion_qs},{inicio},{fin}\n")
        archivo.write(f"Merge sort,{cantidad_de_elementos:.4f},{duracion_ms},{inicio},{fin}\n")



if __name__ == "__main__":
    main()

