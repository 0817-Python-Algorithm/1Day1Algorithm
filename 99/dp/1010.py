def comb(N,M):
    if C[N][M] != 0:
        return C[N][M]
    else:
        if M==0:
            C[N][M] = comb(N-1,M)
            return C[N][M]
        elif M==N:
            C[N][M] = comb(N-1,M-1)
            return C[N][M]
        else:
            C[N][M]= comb(N-1,M-1) + comb(N-1,M)
            return C[N][M]
T = int(input())
C = [[0 for _ in range(i+1)] for i in range(31)]
C[0][0]=1
for t in range(T):
    N,M = map(int,input().split())
    answer = comb(M,N)
    print(answer)
