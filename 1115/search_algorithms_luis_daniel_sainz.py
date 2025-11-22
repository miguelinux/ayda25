# linear (secuential) search
def linear_search(arr, goal):
    for i in range(len(arr)):
        if arr[i] == goal:
            return i
    return -1

# binary search
def binary(arr, goal):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == goal:
            return mid
        elif arr[mid] < goal:
            left = mid + 1
        else:
            right = mid - 1
    return -1
