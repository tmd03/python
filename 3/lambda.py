calculator = lambda n1, n2: n1 + n2
n1 = float(input('n1 : '))
n2 = float(input('n2 : '))
returnValue = calculator(n1, n2)

print(f'returnValue: {returnValue}')


#=================================

tri = lambda n1, n2: n1 * n2 / 2
squ = lambda n1, n2: n1 * n2
cir = lambda r: radius * radius * 3.14

width = int(input('가로 길이 입력: '))
height = int(input('세로 길이 입력: '))
radius = int(input('반지름 길이 입력: '))

triangle = tri(width, height)
square = squ(width, height)
circle = cir(radius)

print(f'삼각형 넓이: {triangle}')
print(f'사각형 넓이: {square}')
print(f'원 넓이: {circle}')