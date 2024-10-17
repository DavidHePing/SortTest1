import heapq
from typing import List

# Context: There are serveral sorted array, need to merge it to a new sorted array
# 
test_case_1 = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]

# Time complexity n*Log(n)
# n means count of all num in arrays
def method1(arrays: List[List[int]]) -> List[int]:
    heap = []
    result = []

    for ary in arrays:
        for num in ary:
            heapq.heappush(heap, num)

    while heap:
        result.append(heapq.heappop(heap))

    return result


# Time complexity n*Log(k)
# n means count of all num in arrays
# k means len(arrays)
def method2(arrays: List[List[int]]) -> List[int]:
    heap = []
    result = []

    for i, array in enumerate(arrays):
        heapq.heappush(heap, (array[0], i, 0))

    while heap:
        num, arrays_index, num_index = heapq.heappop(heap)
        result.append(num)

        num_index += 1

        if num_index < len(arrays[arrays_index]):
            next_num = arrays[arrays_index][num_index]
            heapq.heappush(heap, (next_num, arrays_index, num_index))

    return result

# print(method1(test_case_1))
print(method2(test_case_1))