# w : 쓰기 전용(덮어쓰기), a: 쓰기전용(덧붙임), x: 쓰기 전용(파일 있으면 에러발생), r: 읽기 전용(파일 없으면 에러)
uri = 'C:/pythontxt/'

def writeNumber(n):
    file = open(uri+'text.txt', 'a')
    file.write(str(n))
    file.write('\n')

    file.close()

inputN = int(input('0보다 큰 정수 입력: '))
for number in range(2, (inputN + 1)):
    flag = True
    for n in range(2, number):
        if number % 2 == 0:
            flag = False
            break

    if (flag):
        writeNumber(number)

