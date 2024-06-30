import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    distance, N = map(int, input().rstrip().split(" "))
    places = []
    
    for i in range(N):
        places.append(int(input()))

    places.sort()
    
    max_time = max(distance - places[0], places[-1])
    
    fromMidPlace = [abs(place - distance/2.0) for place in places]
    
    min_distance = 1_000_000
    min_index = 0
    for i in range(N):
        if min_distance > fromMidPlace[i]:
            min_distance = fromMidPlace[i]
            min_index = i
    min_time = min(places[min_index], distance - places[min_index])

    print(min_time, max_time)
