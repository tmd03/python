nums = []
n = 1
while n < 6:

    try:
        num = int(input('input num: '))

    except:
        print('예외')
        continue

    else:
        if num % 2 == 0:
            nums.append(num)
            n += 1

        else:
            print('홀수입니다??', end='')
            continue

print(f'nums: {nums}')