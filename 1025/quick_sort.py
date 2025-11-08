def choose_pivot(arr):
    first = arr[0]
    middle = arr[len(arr)//2]
    last = arr[-1]
    # Devolver la mediana de los tres
    return sorted([first, middle, last])[1]

def sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = choose_pivot(arr)

    return sort([x for x in arr[1:] if x < pivot]) + [pivot] \
        + sort([x for x in arr[1:] if x >= pivot])
