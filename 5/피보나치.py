inputN = int(input('n 입력: '))

valueN = 0
sumN = 0

valueN2 = 0
valueN1 = 0

n = 1
while n <= inputN:
    if n == 1 or n == 2:
        valueN = 1
        valueN2 = valueN
        valueN1 = valueN
        n += 1

    else:
        valueN = valueN2 + valueN1
        valueN2 = valueN1
        valueN1 = valueN
        sumN += valueN
        n += 1

print('{}번째 항의 값: {}'.format(inputN, valueN))
print('{}번째 항까지의 합: {}'.format(inputN, sumN))


#======================================
inputN = int(input('n 입력: '))

result = 1
for n in range(n, inputN+1):
    result *= n

print(f'{inputN} 팩토리얼: {result}')
