a = int(input('첫째항 입력 : '))
r = int(input('공비 입력 : '))
inputn = int(input('n 입력 : '))

valueN = 0
n = 1
while n <= inputn:

    if n == 1 :
        valueN = a
        print(f'{n}번째 항의 값 : {valueN}')
        n += 1
        continue

    valueN *= r
    print(f'{n}번째 항의 값: {valueN}')
    n += 1

print(f'{inputn}번째 항의 값: {valueN}')
