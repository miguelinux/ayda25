#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
"""
Algoritmo de Ordenamiento FULANO
"""
import random
import time

cantidad_de_elmentos = 100
inicio = 0
fin = 100

def ordenar(arr):
    pass

def main():
    """
    Función principal
    """
    lista = [random.randint(inicio,fin) for _ in range(cantidad_de_elmentos) ]
    ordenada = lista.copy()

    tiempo_inicio = time.time()
    ordenar(ordenada)
    tiempo_fin = time.time()

    duracion = tiempo_fin - tiempo_inicio
    print(f"La función se ejecutó en: {duracion:.4f} segundos.")
    print("Lista desordenada", lista)
    print("Lista ordenada", ordenada)


if __name__ == "__main__":
    main()

