N = int(input())
prev = [1] * 10
for i in range(N):
	for j in range(1,10):
		prev[j] = (prev[j-1]+prev[j])%10007
print(prev[9])
