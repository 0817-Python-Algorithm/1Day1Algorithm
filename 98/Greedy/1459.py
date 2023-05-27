x, y, w, s = map(int, input().split())
result = 0
w_count = 0
s_count = 0
if (x + y) % 2 != 0:
    w_count += 1
    if x > y:
        x -= 1
    else:
        y -= 1
# 변 2개해도 대각선보다 짧거나 같을 경우
if 2 * w <= s:
    w_count += x + y
# 변 2개해서는 대각선보다 길지만 1:1 비교시엔 변이 짧을 경우
elif w < s:
    same = min(x, y)
    s_count += same
    w_count += abs(x + y - 2 * same)
# 변 2개해서 대각선보다 길고 1:1 비교시에도 변이 길 경우
else:
    same = min(x, y)
    s_count += same
    s_count += abs(x + y - 2 * same)
print(w * w_count + s * s_count)
