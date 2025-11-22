#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
import random
import time
import csv
# we take the methods from other libraries
from bubble_sort import ordenar as bubble_sort
from bucket_sort import ordenar as bucket_sort
from countingsort import ordenar as counting_sort
from heapsort import ordenar as heap_sort
from insertion_sort import sort as insertion_sort
from merge_sort import ordenar as merge_sort
from quick_sort import sort as quick_sort
from seleccionshort import ordenar as selection_sort
from shellsort import ordenar as shell_sort

# create a list of length n (items_amount) full of random integers
def random_list(items_amount:int) -> list:
    return [random.randint(0, items_amount) for _ in range(items_amount)]

# returns a new ordered list from the given list using the algorithm specified, also returns the time of the process
def ordering(unordered_list:list, algorithm_func:callable) -> tuple[list, float]:
    start_time = time.perf_counter_ns()
    ordered_list = algorithm_func(unordered_list)
    end_time = time.perf_counter_ns()
    total_time = (end_time - start_time) / 1_000
    return ordered_list, total_time

# verificate the right order on the elements in a list
def verification(ordered_list:list) -> bool:
    current_value = -1
    for element in ordered_list:
        if current_value <= element:
            current_value = element
        else:
            return False
    return True

# append results in the archive
def save_results(items_amount:int, algorithm_name:str, ordered:bool, total_time:float):
    with open('tiempos_luis_daniel_sainz.csv', 'a', newline='', encoding='utf-8') as file:
        file.write(f"{items_amount:_},{algorithm_name},{"Sí" if ordered else "No"},{total_time:_}\n")

def main():
    items_amounts = (100, 1_000, 10_000, 100_000, 1_000_000)
    algorithms = (
        ("Bubble Sort", bubble_sort, False),
        ("Bucket Sort", bucket_sort, True),
        ("Counting Sort", counting_sort, True),
        ("Heap Sort", heap_sort, True),
        ("Insertion Sort", insertion_sort, False),
        ("Merge Sort", merge_sort, True),
        ("Quick Sort", quick_sort, True),
        ("Selection Sort", selection_sort, False),
        ("Shell Sort", shell_sort, False),
        )
    # create a new archive for the results
    with open('tiempos_luis_daniel_sainz.csv', 'w', newline='', encoding='utf-8') as file:
        csv.writer(file).writerow(["Elementos", "Algoritmo", "Éxito", "Tiempo (ms)"])

    for amount in items_amounts:
        for algorithm in algorithms:
            algorithm_name = algorithm[0]
            algorithm_func = algorithm[1]
            fast_with_million = algorithm[2]
            if(not(amount == 1_000_000 and not fast_with_million)):
                unordered_list = random_list(amount) 
                ordered_list, total_time = ordering(unordered_list, algorithm_func)
                ordered = verification(ordered_list)
                save_results(amount, algorithm_name, ordered, total_time)

if __name__ == "__main__":
    main()

