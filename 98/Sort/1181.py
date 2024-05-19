from functools import cmp_to_key

def compare(a, b):
    if len(a) < len(b):
        return -1
    elif len(a) == len(b):
        if a > b:
            return 1
        else:
            return -1
    else:
        return 1

N = int(input())

words = set()
for i in range(N):
    words.add(input())

words = list(words)
words.sort(key = len)

for word in words:
    print(word)