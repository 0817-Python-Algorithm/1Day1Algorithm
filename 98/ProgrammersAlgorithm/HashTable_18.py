def solution(arr, target):
    hash_table = [0] * (target+1)
    
    for num in arr:
        if num <= target:
            hash_table[num] = 1
    for num in arr:
        another = target - num
        if (another != num
        and 0 <= another <= target
        and hash_table[another] == 1):
            return True
    return False
print(solution([1,2,3,4,8], 6))
print(solution([2,3,6,7], 7))
print(solution([2,3,5,9], 10))