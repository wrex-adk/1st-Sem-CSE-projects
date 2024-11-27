def selectionSort(array, n):
    for i in range(n-1):
        # Assume the first unsorted element is the smallest
        min_index = i

        # Find the smallest element in the unsorted portion
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j

        # Swap the found minimum element with the first unsorted element
        array[i], array[min_index] = array[min_index], array[i]


data = [-2, 45, 0, 11, -9]
n = len(data)
selectionSort(data, n)
print('Sorted Array in Ascending Order:')
print(data)
