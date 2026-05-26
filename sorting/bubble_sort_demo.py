def bubble_sort(arr):
    n = len(arr)
    for i in range (0,n-1):
        for j in range (0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def bubble_sort(arr):
    sorted = True
    n = len(arr)
    for i in range(0,n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                sorted = False
        if sorted:
            break
    return arr