def partition(arr):
    pivot = arr[-1]
    i = 0
    j = 0

    for i in range(len(arr) - 1):
        if arr[i] < pivot:
            arr[i] , arr[j] = arr[j] , arr[i]
            j +=1
    arr[-1] , arr[j] = arr[j] , arr[-1]
    
    return arr