def ordenar(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    return ordenar([x for x in arr[1:] if x < pivot]) + [pivot] \
        + ordenar([x for x in arr[1:] if x >= pivot])
