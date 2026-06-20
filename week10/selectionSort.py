def selection_sort(arr):
    n = len (arr)
    for i in range(n):
        min_indx = i
        for j in range(i+1, n):
            if arr[min_indx] > arr[j]:
                min_indx = j 
        arr[i], arr[min_indx] = arr[min_indx], arr[i]
        print(f"step {i + 1}: {arr}")

arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("sorted array: ", arr)