def solution(nums):
    nums_set = set(nums)
    
    # 주어진 배열의 길이
    arr_length = len(nums)
    
    # 중복을 제거한 집합의 길이
    set_length = len(nums_set)
    
    # 만약 배열의 절반 개수보다 집합의 개수가 적으면 어쩔 수 없이 집합에 있는 종류들을 총동원해서 뽑을 수 밖에 없음.
    if arr_length/2 > set_length:
        return set_length
    
    # 만약 집합의 개수가 같거나 많으면 그 중 어떤 것이든 중복 없이 arr_length/2개만큼 뽑으면 됨. 
    elif arr_length/2 <= set_length:
        return arr_length/2