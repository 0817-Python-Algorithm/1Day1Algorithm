def solution(bandage, health, attacks):
    t = bandage[0]
    x = bandage[1]
    y = bandage[2]
    sequence = 0
    time = []
    hp = health
    for attack in attacks:
        time.append(attack[0])

    i = 0
    while True:
        i += 1
        if i in time:
            sequence = 0
            hp -= attacks[time.index(i)][1]
            if hp <= 0:
                return -1
        else:
            sequence += 1
            if sequence == t:
                hp += y
                sequence = 0
            hp += x
            if hp > health:
                hp = health
        if i == attacks[-1][0]:
            break        
    return hp

print(solution([5,1,5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]))
print(solution([3,2,7], 20, [[1, 15], [5, 16], [8, 6]]))
print(solution([4,2,7], 20, [[1, 15], [5, 16], [8, 6]]))
print(solution([1,1,1], 5, [[1, 2], [3, 2]]))