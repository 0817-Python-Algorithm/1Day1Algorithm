from itertools import combinations

def find_original_set(subset_sums):
    # 부분집합의 합 배열을 정렬
    subset_sums.sort()
    
    # 원래 집합의 크기 추정
    n = 0
    total_elements = len(subset_sums)
    while 2 ** n < total_elements:
        n += 1
        
    # 0을 제거한 나머지 원소들
    subset_sums = subset_sums[1:]
    
    # 추정된 원래 집합의 원소들을 저장할 리스트
    original_set = []
    
    for _ in range(n):
        # 가장 작은 값이 원래 집합의 원소 중 하나
        smallest = subset_sums[0]
        original_set.append(smallest)
        
        # 원래 집합의 원소에 대한 부분집합 합을 제거
        new_subset_sums = []
        for sum_value in subset_sums:
            if sum_value - smallest in subset_sums:
                subset_sums.remove(sum_value - smallest)
            else:
                new_subset_sums.append(sum_value)
                
        subset_sums = new_subset_sums
    
    return original_set

# 예시 사용법
subset_sums = [0, 2, 3, 5, 7, 8, 10, 15]
original_set = find_original_set(subset_sums)
print(f"원래 집합의 숫자들: {original_set}")
