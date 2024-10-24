def mergeSort(arr: list, start: int, end: int) -> list:
    if start >= end:
        return [arr[start]]
    
    if end - start == 1:
        return [arr[start], arr[end]]
    
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

    return result

l1 = [0, 6, 73, 18, 84, 81, 57, 77, 83, 78, 71, 67, 36, 93, 93, 33, 70, 100, 84, 64]

print(mergeSort(l1, 0, len(l1) - 1))


    