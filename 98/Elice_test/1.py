import sys
import itertools

input = sys.stdin.readline().rstrip

num = int(input())

numbers = list(str(num))

permutatoins = sorted(itertools.permutations(numbers))

cases = []
for permutation in permutatoins:
    cases.append(int("".join(permutation)))

cases = list(set(cases))

if cases.index(num)+1 < len(cases):
    print(cases[cases.index(num)+1])