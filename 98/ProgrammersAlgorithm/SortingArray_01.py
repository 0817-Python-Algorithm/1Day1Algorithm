import time

# 원본 유지하지 못한 채 정렬
def solution1(arr):
    arr.sort()
    return arr

# 원본 유지한 채 정렬
def solution2(arr):
    sorted_list = arr
    sorted_list.sort()
    return sorted_list

# 버블 정렬 사용(O(N^2))
def bubbleSort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 버블정렬(O(N^2))과 sort()함수(O(NlogN))의 시간 비교
def timeTest(func, arr):
    startTime = time.time()
    result = func(arr)
    endTime = time.time()
    return endTime - startTime, result

arr = list(range(100000))
bubbleSort_time, bubbleSort_result = timeTest(bubbleSort, arr)
arr = list(range(100000))
solution2_time, solution2_result = timeTest(solution2, arr)

print(f'{"버블 정렬한 결과 걸린 시간:":<25} {bubbleSort_time}')
print(f'{"sort함수 사용한 결과 걸린 시간:":<25} {solution2_time}')
print(f'{"결과가 동일한지 여부:":<25} {bubbleSort_result == solution2_result}')