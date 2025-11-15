#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
"""
Comparación de todos los métodos de ordenamiento
"""
import random
import time
import csv

# Importamos todos los métodos de ordenamiento disponibles
from bubble_sort import ordenar as bubble_sort
from bucket_sort import ordenar as bucket_sort
from countingsort import ordenar as counting_sort
from heapsort import ordenar as heap_sort
from insertion_sort import sort as insertion_sort
from quick_sort import sort as quick_sort
from seleccionshort import ordenar as selection_sort
from shellsort import ordenar as shell_sort

# Merge sort personalizado (el original tiene un bug con variable global)
def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    sorted_result = []
    i_left = 0
    i_right = 0

    while i_left < len(left) and i_right < len(right):
        if left[i_left] < right[i_right]:
            sorted_result.append(left[i_left])
            i_left += 1
        else:
            sorted_result.append(right[i_right])
            i_right += 1

    sorted_result.extend(left[i_left:])
    sorted_result.extend(right[i_right:])

    return sorted_result


def random_list(items_amount: int) -> list:
    """Crea una lista de longitud n con enteros aleatorios"""
    return [random.randint(0, items_amount) for _ in range(items_amount)]


def ordering(unordered_list: list, algorithm_func: callable) -> tuple:
    """Retorna la lista ordenada y el tiempo de ejecución en microsegundos"""
    start_time = time.perf_counter_ns()
    ordered_list = algorithm_func(unordered_list)
    end_time = time.perf_counter_ns()
    total_time = (end_time - start_time) / 1_000  # nanosegundos a microsegundos
    return ordered_list, total_time


def verification(ordered_list: list) -> bool:
    """Verifica que la lista esté correctamente ordenada"""
    for i in range(len(ordered_list) - 1):
        if ordered_list[i] > ordered_list[i + 1]:
            return False
    return True


def save_results(items_amount: int, algorithm_name: str, ordered: bool, total_time: float):
    """Guarda los resultados en el archivo CSV"""
    with open('tiempos_amora.csv', 'a', newline='', encoding='utf-8') as file:
        success = "Sí" if ordered else "No"
        file.write(f"{items_amount:_},{algorithm_name},{success},{total_time:_.2f}\n")


def main():
    items_amounts = (100, 1_000, 10_000, 100_000, 1_000_000)

    # (nombre, función, es_rapido_con_millon)
    algorithms = (
        ("Bubble Sort", bubble_sort, False),
        ("Bucket Sort", bucket_sort, True),
        ("Counting Sort", counting_sort, True),
        ("Heap Sort", heap_sort, True),
        ("Insertion Sort", insertion_sort, False),
        ("Merge Sort", merge_sort, True),
        ("Quick Sort", quick_sort, True),
        ("Selection Sort", selection_sort, False),
        ("Shell Sort", shell_sort, True),
    )

    # Crear archivo CSV con encabezados
    with open('tiempos_amora.csv', 'w', newline='', encoding='utf-8') as file:
        csv.writer(file).writerow(["Elementos", "Algoritmo", "Éxito", "Tiempo (µs)"])

    total_tests = sum(1 for amount in items_amounts for alg in algorithms
                      if not (amount == 1_000_000 and not alg[2]))
    current_test = 0

    for amount in items_amounts:
        print(f"\n--- Probando con {amount:,} elementos ---")
        for algorithm in algorithms:
            algorithm_name = algorithm[0]
            algorithm_func = algorithm[1]
            fast_with_million = algorithm[2]

            # Saltar algoritmos lentos para 1 millón de elementos
            if amount == 1_000_000 and not fast_with_million:
                print(f"  {algorithm_name}: Omitido (muy lento para 1M elementos)")
                continue

            current_test += 1
            print(f"  [{current_test}/{total_tests}] {algorithm_name}...", end=" ", flush=True)

            unordered_list = random_list(amount)
            ordered_list, total_time = ordering(unordered_list, algorithm_func)
            ordered = verification(ordered_list)
            save_results(amount, algorithm_name, ordered, total_time)

            status = "OK" if ordered else "FALLO"
            print(f"{status} - {total_time:,.2f} µs")

    print(f"\nResultados guardados en 'tiempos_amora.csv'")


if __name__ == "__main__":
    main()
