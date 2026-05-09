def selection(arr):
    for i in range (len(arr)):
        element = arr[i]
        index_of_min=i
        for j in range (i+1,len(arr)):
            if element > arr[j]:
                index_of_min = j
                element = arr[j]
        arr[index_of_min] , arr[i] = arr[i] , arr[index_of_min]
    return arr