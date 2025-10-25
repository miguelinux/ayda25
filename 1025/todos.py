#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
"""
Algoritmo de Ordenamiento FULANO
"""
import random
import time

from quicksort import ordenar as qs

cantidad_de_elementos = 100
inicio = 0
fin = 100

def main():
    """
    Función principal
    """
    lista = [random.randint(inicio,fin) for _ in range(cantidad_de_elementos) ]
    #ordenada = lista.copy()

    tiempo_inicio = time.time()
    ordenada = qs(lista)
    tiempo_fin = time.time()

    tiempo_qs = tiempo_fin - tiempo_inicio

    with open("tiempos.csv","w", encoding="utf-8") as archivo:
        archivo.write("Algoritmo,Cantidad de elementos,Tiempo,Inicio,Fin\n")
        archivo.write(f"Quicksort,{cantidad_de_elementos:.4f},{tiempo_qs},{inicio},{fin}\n")

    #print(f"La función se ejecutó en: {duracion:.4f} segundos.")
    #print("Lista desordenada", lista)
    #print("Lista ordenada", ordenada)


if __name__ == "__main__":
    main()

