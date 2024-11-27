def selectionSort(arr, n):
    for s in range(n):
        min_idx = s
        for i in range(s + 1, n):
            # Find the minimum element in the remaining array
            if arr[i] < arr[min_idx]:
                min_idx = i
        # Swap the found minimum element with the first element of the unsorted part
        (arr[s], arr[min_idx]) = (arr[min_idx], arr[s])

arr = [7, 2, 1, 6]
n = len(arr)
selectionSort(arr, n)
print("Sorted array:", arr)


