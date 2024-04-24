evelist = [] ; oddlist = [] ; floatlist = []
nums = []

n = 1
while n < 6:

    try:
        num = input('input num: ')
        numflo = float(num)

    except:
        print('숫자입력!!!')
        continue

    else:
        if numflo - int(numflo) != 0:
            print('실수!!!!')
            floatlist.append(numflo)
        else:
            if numflo % 2 == 0 :
                print('짝수!!!!')
                evelist.append(numflo)
            else:
                print('홀수!!!!')
                oddlist.append(numflo)

        n += 1
    finally:
        nums.append(num)

print(f'nums : {nums}')
print(f'evelist : {evelist}')
print(f'oddlist : {oddlist}')
print(f'floatlist : {floatlist}')
