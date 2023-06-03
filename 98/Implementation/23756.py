n = int(input())
result = 0
standard = int(input())
for i in range(n):
    test = int(input())
    if standard < test:
        if test - standard < standard - test + 360:
            result += test - standard
        else:
            result += standard - test + 360

    else:
        if standard - test < test - standard + 360:
            result += standard - test
        else:
            result += test - standard + 360
    standard = test
print(result)