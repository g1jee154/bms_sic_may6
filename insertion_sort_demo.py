def insertion(arr):
    n = len(arr)
    for i in range(n):
        element = arr[i]
        j = i - 1
        while element < arr[j] and j>=0:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = element
    return arr
