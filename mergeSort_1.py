def mergeSort(arr: list, start: int, end: int) -> list:
    if start > end:
        return []

    if start == end:
        return [arr[start]]
    
    if end - start == 1:
        bigger = max(arr[start], arr[end])
        smaller = min(arr[start], arr[end])
        return [smaller, bigger]
    
    mid = start + (end - start) // 2
    left_ary = mergeSort(arr, start, mid)
    right_ary = mergeSort(arr, mid + 1, end)

    left = 0
    right = 0    
    result = []

    while left < len(left_ary) and right < len(right_ary):
        if left_ary[left] < right_ary[right]:
            result.append(left_ary[left])
            left += 1
        else:
            result.append(right_ary[right])
            right += 1

    while left < len(left_ary):
        result.append(left_ary[left])
        left += 1

    while right < len(right_ary):
        result.append(right_ary[right])
        right += 1

    # print(left_ary, right_ary)
    # print(result)
    return result

# Testing the function with your lists
l1 = [0, 6, 73, 18, 84, 81, 57, 77, 83, 78, 71, 67, 36, 93, 93, 33, 70, 100, 84, 64]
print(mergeSort(l1, 0, len(l1) - 1))

# Test Case 1: An already sorted array (best case)
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Sorted array:", mergeSort(sorted_array, 0, len(sorted_array) - 1))

# Test Case 2: A reverse-sorted array (worst case)
reverse_sorted_array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Reverse sorted array:", mergeSort(reverse_sorted_array, 0, len(reverse_sorted_array) - 1))

# Test Case 3: An array with duplicate values
array_with_duplicates = [5, 1, 7, 7, 2, 2, 5, 8, 1, 3]
print("Array with duplicates:", mergeSort(array_with_duplicates, 0, len(array_with_duplicates) - 1))

# Test Case 4: An array with negative numbers
array_with_negatives = [-10, 3, 0, -2, 5, -1, 4]
print("Array with negatives:", mergeSort(array_with_negatives, 0, len(array_with_negatives) - 1))

# Test Case 5: A single-element array
single_element_array = [42]
print("Single element array:", mergeSort(single_element_array, 0, len(single_element_array) - 1))

# Test Case 6: An empty array
empty_array = []
print("Empty array:", mergeSort(empty_array, 0, len(empty_array) - 1))

# Test Case 7: A large array with random values
import random
large_array = [random.randint(1, 1000) for _ in range(100)]
print("Large array sorted:", mergeSort(large_array, 0, len(large_array) - 1))


    