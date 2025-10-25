#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
"""
Insertion Sort Algorithm
"""
import random
import time
import math

number_of_elements = 100
start = 0
end = 100


def sort(arr: list) -> list:
    """
    Insertion Sort:
    Builds the sorted list one item at a time by inserting each element
    into its correct position among the previously sorted elements.
    """
    # BASE CASE - Lists with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr

    # ITERATIVE CASE
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements greater than 'key' one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

        # Uncomment this line if you want to see progress at each iteration
        # print(f"Step {i}: {arr}")

    return arr


def main():
    """
    Main function to test the insertion sort algorithm.
    """
    lst = [random.randint(start, end) for _ in range(number_of_elements)]
    sorted_list = lst.copy()

    time_start_ns = time.perf_counter_ns()
    sort(sorted_list)
    time_end_ns = time.perf_counter_ns()

    duration_us = (time_end_ns - time_start_ns) / 1000  # Convert ns → µs

    print(f"Execution time: {duration_us:.3f} microseconds.")
    print("Unsorted list:", lst)
    print("Sorted list:", sorted_list)


if __name__ == "__main__":
    main()
