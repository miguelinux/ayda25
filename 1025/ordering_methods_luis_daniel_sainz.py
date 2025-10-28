#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
import random
import time
import csv
# we take the methods from other libraries
from quick_sort import sort as quick_sort
from merge_sort import ordenar as merge_sort
from insertion_sort import sort as insertion_sort

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
    with open('tarea.csv', 'a', newline='', encoding='utf-8') as file:
        file.write(f"{items_amount:_}, {algorithm_name}, {"Sí" if ordered else "No"}, {total_time:_}\n")

def main():
    items_amounts = (100, 1_000, 10_000, 100_000, 1_000_000)
    algorithms = (
        ("Quick Sort", quick_sort),
        ("Merge Sort", merge_sort),
        ("Insertion Sort", insertion_sort)
        )
    # create a new archive for the results
    with open('tarea.csv', 'w', newline='', encoding='utf-8') as file:
        csv.writer(file).writerow(["Cantidad de Elementos", "Algoritmo", "Éxito", "Tiempo (microsegundos)"])

    for amount in items_amounts:
        for algorithm in algorithms:
            algorithm_name = algorithm[0]
            algorithm_func = algorithm[1]
            unordered_list = random_list(amount) 
            ordered_list, total_time = ordering(unordered_list, algorithm_func)
            ordered = verification(ordered_list)
            save_results(amount, algorithm_name, ordered, total_time)

if __name__ == "__main__":
    main()

