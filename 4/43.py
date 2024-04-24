nums = []
n = 1
while n < 6:

    try:
        num = input('input num: ')
        numint = int(num)

    except:
        print('숫자입력!!!')
        numflo = 0  # =continue

    else:
        if n % 2 == 0 :
            print('짝수!!!!')
        else:
            print('홀수!!!!')

    finally:
        print(f'inputData: {num}')


nums.append(num)
n += 1

print(f'nums: {nums}')