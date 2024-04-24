n1 = int(input('a1 입력: '))
d = int(input('공차 입력: '))
inputn = int(input('n 입력: '))

valueN = 0
sumN = 0

# 등차 수열 합 공식 : sn = n(a1 + an) / 2
valueN = n1 + (inputn-1) * d
sumN = inputn * (n1 + valueN) / 2
print(f'{inputn}번째 항까지의 합: {int(sumN)}')

#=======================================
n1 = int(input('a1 입력: '))
r = int(input('공비 입력: '))
inputn = int(input('n 입력: '))

valueN = 0
sumN = 0

# 등비수열 공식: sn = a1 * (1 - r^n) / (1-r)
sumN = n1 * (1 - (r ** inputn)) / (1-r)
print(f'{inputn}번째 항까지의 합: {int(sumN)}')