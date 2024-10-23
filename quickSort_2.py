l1 = [0, 6, 73, 18, 84, 81, 57, 77, 83, 78, 71, 67, 36, 93, 93, 33, 70, 100, 84, 64]
l2 = [9, 4, 1, 6, 7, 3, 8, 2, 5]
l3 = [3, 8, 2, 5, 1, 4, 7, 6]
l4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l5 = [9, 8, 7, 6, 5, 4, 3, 2, 1]

def quickSort(arr: list, start: int, end: int):
    if start >= end:
        return 0

    mid = start + (end - start) // 2
    arr[mid], arr[end] = arr[end], arr[mid]
    pivot = arr[end]
    
    left = 0
    
    for right in range(end):
        if arr[right] <= pivot:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
    
    arr[left], arr[end] = arr[end], arr[left]

    new_pivot = left
    quickSort(arr, 0, new_pivot - 1)
    quickSort(arr, new_pivot + 1, end)


quickSort(l1, 0, len(l1) - 1)
print(l1)
quickSort(l2, 0, len(l2) - 1)
print(l2)
quickSort(l3, 0, len(l3) - 1)
print(l3)
quickSort(l4, 0, len(l4) - 1)
print(l4)
quickSort(l5, 0, len(l5) - 1)
print(l5)