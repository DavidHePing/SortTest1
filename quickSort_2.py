def quickSort(arr: list, start: int, end: int):
    if start >= end:
        return

    mid = start + (end - start) // 2
    arr[mid], arr[end] = arr[end], arr[mid]
    pivot = arr[end]
    
    left = start
    
    for right in range(start, end):
        if arr[right] <= pivot:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
    
    arr[left], arr[end] = arr[end], arr[left]

    new_pivot = left
    quickSort(arr, start, new_pivot - 1)
    quickSort(arr, new_pivot + 1, end)

# Testing the function with your lists
l1 = [0, 6, 73, 18, 84, 81, 57, 77, 83, 78, 71, 67, 36, 93, 93, 33, 70, 100, 84, 64]

quickSort(l1, 0, len(l1) - 1)
print(l1)

# Test Case 1: An already sorted array (best case)
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
quickSort(sorted_array, 0, len(sorted_array) - 1)
print("Sorted array:", sorted_array)

# Test Case 2: A reverse-sorted array (worst case)
reverse_sorted_array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
quickSort(reverse_sorted_array, 0, len(reverse_sorted_array) - 1)
print("Reverse sorted array:", reverse_sorted_array)

# Test Case 3: An array with duplicate values
array_with_duplicates = [5, 1, 7, 7, 2, 2, 5, 8, 1, 3]
quickSort(array_with_duplicates, 0, len(array_with_duplicates) - 1)
print("Array with duplicates:", array_with_duplicates)

# Test Case 4: An array with negative numbers
array_with_negatives = [-10, 3, 0, -2, 5, -1, 4]
quickSort(array_with_negatives, 0, len(array_with_negatives) - 1)
print("Array with negatives:", array_with_negatives)

# Test Case 5: A single-element array
single_element_array = [42]
quickSort(single_element_array, 0, len(single_element_array) - 1)
print("Single element array:", single_element_array)

# Test Case 6: An empty array
empty_array = []
quickSort(empty_array, 0, len(empty_array) - 1)
print("Empty array:", empty_array)

# Test Case 7: A large array with random values
import random
large_array = [random.randint(1, 1000) for _ in range(100)]
quickSort(large_array, 0, len(large_array) - 1)
print("Large array sorted:", large_array)

