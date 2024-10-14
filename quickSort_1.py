l = [0, 6, 73, 18, 84, 81, 57, 77, 83, 78, 71, 67, 36, 93, 93, 33, 70, 100, 84, 64]

def quickSort(arr: list) -> list:
    if not arr:
        return arr

    pivot = arr[len(arr) // 2]
    left = [num for num in arr if num < pivot]
    mid = [num for num in arr if num == pivot]
    right = [num for num in arr if num > pivot]

    return quickSort(left) + mid + quickSort(right)

print(quickSort(l))