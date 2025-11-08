#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
"""
Algoritmo de Ordenamiento por Conteo (Counting Sort) Giovanna
"""
import random
import time

cantidad_de_elementos = 100
inicio = 0
fin = 100

def ordenar(arr):
    # 1. Encontrar el valor máximo para determinar el tamaño del array de conteo
    max_val = max(arr)
    size = len(arr)
    
    # Inicializar el array de salida (output) y el array de conteo (count)
    output = [0] * size
    count = [0] * (max_val + 1)
    
    # 2. y 3. Contar las ocurrencias de cada elemento
    for i in range(size):
        count[arr[i]] += 1
    
    # 4. Calcular la suma acumulada (para estabilidad y posiciones finales)
    for i in range(1, max_val + 1):
        count[i] += count[i - 1]
    
    # 5. Colocar los elementos en el array de salida (recorriendo al revés para estabilidad)
    # Recorrer desde el último elemento al primero.
    i = size - 1
    while i >= 0:
        # La posición final es count[arr[i]] - 1
        current_element = arr[i]
        final_position = count[current_element] - 1
        output[final_position] = current_element
        
        # Decrementar el contador para el próximo elemento con el mismo valor
        count[current_element] -= 1
        i -= 1
        
    # Copiar los elementos ordenados al array original (opcional, o retornar 'output')
    for i in range(size):
        arr[i] = output[i]
   
    return arr

def main():
    """
    Función principal
    """
    lista = [random.randint(inicio,fin) for _ in range(cantidad_de_elementos) ]
    ordenada = lista.copy()

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

