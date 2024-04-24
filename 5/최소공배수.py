n1 = int(input('1보다 큰 정수 입력: '))
n2 = int(input('1보다 큰 정수 입력: '))
n3 = int(input('1보다 큰 정수 입력: '))

for i in range(1, (n1+1)):
    if n1 % i == 0 and n2 % 1 == 0:
        print(f'공약수: {i}')
        maxNum = i

print(f'최대공약수 : {maxNum}')

minNum = (n1 * n2) // maxNum
print(f'{n1}, {n2} 최소공배수 : {minNum}')

newNum = minNum
for i in range (1, (newNum+1)):
    if newNum % i == 0 and n3 % i == 0:
        maxNum = i

print(f'최대공약수 : {maxNum}')

minNum = (newNum * n3) // maxNum
print(f'{n1}, {n2}, {n3}의 최소공배수 : {minNum}')

