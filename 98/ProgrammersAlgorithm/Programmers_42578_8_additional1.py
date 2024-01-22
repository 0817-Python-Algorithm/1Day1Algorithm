def solution(clothes):
    
    # 옷을 카테고리(key)별 제품명(value)으로 저장할 dictionary
    cloth_table = {}
    
    # cloths를 돌면서 set타입의 value에 추가해나감.
    for cloth in clothes:
        name, category = cloth

        if category in cloth_table:
            cloth_table[category].add(name)
        else:
            cloth_table[category] = set([name])
        
    answer = 1
    for v in cloth_table.values():
        # 해당 종류에서 아무것도 착용하지 않는 경우가 있기에 +1한 뒤 곱함
        answer *= (len(v)+1)
    # 단 하나도 착용하지 않은 경우는 빼줘야 하므로 -1을 함
    answer -= 1
    return answer

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))