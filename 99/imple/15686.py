import copy
N, chicken = map(int, input().split())

mymap = []
chicken_index = []
house_index = []
for i in range(N):
    mymap.append(list(map(int, input().split())))
    for j in range(N):
        if mymap[i][j] == 2:
            chicken_index.append((i,j))
        elif mymap[i][j] == 1:
            house_index.append((i,j))
# global answer = 0
answer = 2000
def comb(c, index,depth):
    global answer
    global chicken
    if chicken == depth:
        # todo
        chicken_dist = 0
        for house in house_index:
            min_dist = 2000
            for tmp in c:
                chic = chicken_index[tmp]
            # for chic in chicken_index[c]:
                dist = abs(house[0]-chic[0]) + abs(house[1]-chic[1])
                min_dist = min(min_dist,dist)
            chicken_dist += min_dist
        # print(chicken_dist)
        if answer > chicken_dist:
            answer = chicken_dist
        return
    else:
        for i in range(index, len(chicken_index)):
            c.append(i)
            comb(copy.deepcopy(c), i+1, depth+1)
            c.pop()
comb([],0,0)
print(answer)