n1 = int(input('1보다 큰 정수 입력: '))
n2 = int(input('1보다 큰 정수 입력: '))

temp1 = n1; temp2 = n2

while temp2 > 0:
    temp = temp2
    temp2 = temp1 % temp2
    temp1 = temp

print(f'{n1}, {n2}의 최대공약수 : {temp1}')

for n in range(1, (temp1+1)):
    if temp1 % n == 0:
        print(f'{n1},{n2}의 공약수: {n}')