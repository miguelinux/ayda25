def sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    return sort([x for x in arr[1:] if x < pivot]) + [pivot] \
        + sort([x for x in arr[1:] if x >= pivot])
