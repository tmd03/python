def calculator(n1, n2, operator):

    def addCal():
        print(f'덧셈 연산: {round(n1 + n2, 2)}')

    def minCal():
        print(f'뺼셈 연산: {round(n1 - n2, 2)}')

    def mulCal():
        print(f'곱셈 연산: {round(n1 * n2, 2)}')

    def divCal():
        print(f'나눗셈 연산: {round(n1 / n2, 2)}')

    if operator == 1:
        addCal()
    elif operator == 2:
        minCal()
    elif operator == 3:
        mulCal()
    elif operator == 4:
        divCal()

while True:
    n1 = float(input('실수(n1) 입력: '))
    n2 = float(input('실수(n2) 입력: '))
    operator = int(input('1.덧셈, 2.뺄셈, 3.곱셈, 4.나눗셈, 5.종료  '))

    if operator == 5:
        print('bye~~')
        break

    calculator(n1, n2, operator)