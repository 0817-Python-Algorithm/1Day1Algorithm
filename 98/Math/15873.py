import sys
input = sys.stdin.readline

str = input()

tenPlace = str.find("0")

# 0이 존재하지 않으면 두 글자 더하기
if tenPlace == -1:
    print(int(str[0])+int(str[1]))
# 0이 존재하면...
else:
    # 만약 0이 2번째 글자에 있으면 앞 숫자 = 10, 뒷 숫자 = 나머지(10일 수도 아닐 수도)
    if tenPlace == 1:
        print(10 + int(str[2:]))
    # 만약 0이 2번째 글자에 없으면 앞 숫자 = 한자리 숫자, 뒷 숫자 = 10
    else:
        print(int(str[0]) + 10)