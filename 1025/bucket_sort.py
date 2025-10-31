#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
"""
Algoritmo de Ordenamiento Bucket Sort
"""
import random
import time

cantidad_de_elementos = 100
inicio = 0
fin = 100

def ordenar(arr: list) -> list:
    # Si la lista está vacía o tiene un solo elemento, no hay nada que ordenar
    if len(arr) <= 1:
        return arr
    
    # Encontramos el valor máximo y el valor mínimo de la lista
    max_val = max(arr)
    min_val = min(arr)
    
    # Número de "buckets" o cubos que vamos a usar
    num_buckets = 10
    
    # Ancho de cada bucket
    bucket_range = (max_val - min_val) / num_buckets
    
    # Crear los cubos vacíos
    buckets = [[] for _ in range(num_buckets)]
    
    # Distribuimos los elementos en los cubos
    for num in arr:
        # Usamos la fórmula para determinar el índice del cubo para cada número
        index = int((num - min_val) // bucket_range)
        if index == num_buckets:  # Para manejar el caso en que el número es el máximo
            index -= 1
        buckets[index].append(num)
    
    # Ordenamos los elementos dentro de cada cubo (usamos sort de Python)
    for i in range(num_buckets):
        buckets[i].sort()
    
    # Concatenamos los cubos ya ordenados
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
    
    return sorted_arr

def main():
    """
    Función principal
    """
    lista = [random.randint(inicio, fin) for _ in range(cantidad_de_elementos)]
    ordenada = lista.copy()

    # Medición de tiempo
    tiempo_inicio_ns = time.perf_counter_ns()

    # Ordenación
    ordenada = ordenar(ordenada)

    tiempo_fin_ns = time.perf_counter_ns()

    # Calcular la duración en segundos
    duracion_s = (tiempo_fin_ns - tiempo_inicio_ns) / 1_000_000_000  # Convirtiendo de ns a segundos

    # Imprimir resultados
    print("Lista desordenada:", lista)
    print("Lista ordenada:", ordenada)
    print(f"La función se ejecutó en: {duracion_s:.6f} segundos.")

if __name__ == "__main__":
    main()
