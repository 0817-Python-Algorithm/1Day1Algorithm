def solution(arr):
    # set으로 중복이 없도록 만들고 list로 변환
    # 이때, set의 시간 복잡도는 O(N)이다.
    # sort하는 과정의 시간 복잡도는 O(NlogN)이기 때문에,
    # 최종 시간 복잡도는 O(NlogN)
    newArr = list(set(arr))
    newArr.sort(reverse = True)
    return newArr

arr = [1,5,77,32,10,9]
print(solution(arr))
