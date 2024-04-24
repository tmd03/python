
def calculator(n1, n2, a):

    def addCal():
        print(f'{n1} + {n2} = {n1 + n2}')

    def minCal():
        print(f'{n1} - {n2} = {n1 - n2}')

    def mulCal():
        print(f'{n1} * {n2} = {n1 * n2}')

    def divCal():
        print(f'{n1} / {n2} = {n1 / n2}')

    def skajwlCal():
        print(f'{n1} % {n2} = {n1 % n2}')

    def ahrtCal():
        print(f'{n1} // {n2} = {n1 // n2}')

    def wprhqCal():
        print(f'{n1} ** {n2} = {n1 ** n2}')

    if a == 1:
        addCal()
    elif a == 2:
        minCal()
    elif a == 3:
        mulCal()
    elif a == 4:
        divCal()
    elif a == 5:
        skajwlCal()
    elif a == 6:
        ahrtCal()
    elif a == 7:
        wprhqCal()



while True:
    print('-' * 30)
    a = int(input('1.덧셈, 2.뺄셈, 3.곱셈, 4.나눗셈, 5.나머지, 6.몫, 7.제곱승, 8.종료: '))
    n1 = float(input('첫번째 숫자 입력: '))
    n2 = float(input('두번째 숫자 입력: '))
    print('-' * 30)
    print('-' * 30)

    if a == 8:
        print('bye~~')
        break

    calculator(n1,n2, a)
