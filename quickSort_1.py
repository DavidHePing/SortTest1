l = [0, 6, 73, 18, 84, 81, 57, 77, 83, 78, 71, 67, 36, 93, 93, 33, 70, 100, 84, 64]

def quickSort(arr: list) -> list:
    if not arr:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)

print(quickSort(l))