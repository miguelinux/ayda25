#! /usr/bin/env python3
# Algoritmo de ordenamiento de Eduardo Aleman

import random
import time

cantidad_de_elementos = 1000000
inicio = 0
fin = cantidad_de_elementos

def ordenar(arr):
    """Ordena una lista usando el método Heapsort."""

    def heapify(arr, n, i):
        """Ajusta el subárbol con raíz en el índice i para mantener la propiedad de montículo máximo."""
        mayor = i
        izquierda = 2 * i + 1
        derecha = 2 * i + 2

        # Si el hijo izquierdo es mayor que la raíz
        if izquierda < n and arr[izquierda] > arr[mayor]:
            mayor = izquierda

        # Si el hijo derecho es mayor que el más grande actual
        if derecha < n and arr[derecha] > arr[mayor]:
            mayor = derecha

        # Si el mayor no es la raíz
        if mayor != i:
            arr[i], arr[mayor] = arr[mayor], arr[i]
            # Llamada recursiva para ajustar el subárbol afectado
            heapify(arr, n, mayor)

    n = len(arr)

    # Construir el montículo (reorganizar la lista)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraer los elementos del montículo uno por uno
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Intercambiar el máximo al final
        heapify(arr, i, 0)

    return arr


def main():
    lista = [random.randint(inicio, fin) for _ in range(cantidad_de_elementos)]
    ordenada = lista.copy()

    tiempo_inicio = time.perf_counter_ns()
    ordenar(ordenada)  # llamada a la función de ordenamiento
    tiempo_fin = time.perf_counter_ns()
    duracion = (tiempo_fin - tiempo_inicio)/1000

    print(f"La función se ejecutó en: {duracion:.4f} micro segundos.")
    print("Lista desordenada:\n", lista)
    print("Lista ordenada:\n", ordenada)


if __name__ == "__main__":
    main()