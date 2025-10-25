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


def main():
    """
    Función principal
    """
    lista = [random.randint(inicio,fin) for _ in range(cantidad_de_elementos) ]

    desordenada = lista.copy()
    tiempo_inicio = time.perf_counter_ns()
    ordenada = qs(desordenada)
    tiempo_fin = time.perf_counter_ns()
    duracion_qs = (tiempo_fin - tiempo_inicio) / 1000  # Convirtiendo de ns a us
    verifica(ordenada, "Quicksort")

    desordenada = lista.copy()
    tiempo_inicio = time.perf_counter_ns()
    ordenada = ms(desordenada)
    tiempo_fin = time.perf_counter_ns()
    duracion_ms = (tiempo_fin - tiempo_inicio) / 1000  # Convirtiendo de ns a us
    verifica(ordenada, "Merge sort")

    with open("tiempos.csv","w", encoding="utf-8") as archivo:
        archivo.write("Algoritmo,Cantidad de elementos,Tiempo,Inicio,Fin\n")
        archivo.write(f"Quicksort,{cantidad_de_elementos:.4f},{duracion_qs},{inicio},{fin}\n")
        archivo.write(f"Merge sort,{cantidad_de_elementos:.4f},{duracion_ms},{inicio},{fin}\n")

    #print(f"La función se ejecutó en: {duracion:.4f} segundos.")
    #print("Lista desordenada", lista)
    #print("Lista ordenada", ordenada)


if __name__ == "__main__":
    main()

