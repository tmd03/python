a = int(input('첫째항 입력 : '))
d = int(input('공차 입력 : '))
inputn = int(input('n 입력 : '))

valueN = 0
n = 1
while n <= inputn:

    if n == 1 :
        valueN = a
        print(f'{n}번째 항의 값 : {valueN}')
        n += 1
        continue

    valueN += d
    print(f'{n}번째 항의 값: {valueN}')
    n += 1

print(f'{inputn}번째 항의 값: {valueN}')

#====================================
a = int(input('첫째항 입력 : '))
d = int(input('공차 입력 : '))
inputn = int(input('n 입력 : '))
valueN = 0

valueN = a + (inputn - 1) * d
print(f'{inputn}번째 항의 값: {valueN}')