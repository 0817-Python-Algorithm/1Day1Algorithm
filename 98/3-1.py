n, m, k = map(int, input().split()) #n,m,k 값 받아옴
data = list(map(int, input().split())) #재료로 쓰일 숫자 배열 받아옴

#정렬을 통해 1,2번째로 큰 수를 각각 num1, num2에 넣음
data.sort()
num1 = data[n - 1]
num2 = data[n - 2]
result = 0

while True:
    for j in range(k): #가장 큰 수를 k번씩 씀
        result += num1
        m = m - 1
        if m == 0: break #m개 채우면 break
    if m == 0: break #m개 채우면 break
    result += num2 #두번째 큰 수를 한번 써줌
    m = m - 1
    if m == 0: break #m개 채우면 break

print(result)
