nums = []
n = 1
while n < 6:

    try:
        num = float(input('input num: '))

    except:
        print('숫자입력!!!')
        continue

    else:
        if num - int(num) != 0:
            print('실수!!!!')
        else:
            if n % 2 == 0 :
                print('짝수!!!!')
            else:
                print('홀수!!!!')

    nums.append(num)
    n += 1
print(f'nums: {nums}')