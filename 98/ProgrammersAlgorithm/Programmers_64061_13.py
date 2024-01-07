def solution(board, moves):

    l = len(board)
    
    basket = []
    
    stack = [[] for _ in range(l)]
    
    # 들어온 input 자체가 거꾸로 들어온 경우엔,
    # input 배열을 거꾸로 돌면서 push 해주면 됨.
    for i in range(l - 1, -1, -1):
        for j in range(l):
            if board[i][j] != 0:
                stack[j].append(board[i][j])

    for move in moves:
        if stack[move-1]:
            basket.append(stack[move-1].pop())
    
    if len(basket) == 0:
        return 0

    new_basket = [basket[0]]
    answer = 0

    for i in range(1, len(basket)):

        # 여기서도 앞서와 마찬가지로 배열이 비어있는 경우를 고려해서 검사를 해줘야 함.
        if new_basket and new_basket[-1] == basket[i]:
            new_basket.pop()
            answer += 2
        else:
            new_basket.append(basket[i])
        
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))