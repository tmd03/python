inputnum = int(input('1보다 큰 정수 입력: '))

n = 2
while n <= inputnum:
    if inputnum % n == 0 :
        print('소인수: {}'.format(n))
        inputnum /= n
    else:
        n += 1