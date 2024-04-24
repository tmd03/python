n1= 10; n2 = 0

print(n1+n2)
print(n1-n2)
print(n1*n2)
try:
    print(n1/n2)
except:
    print('예외')

#======================
nums = []

n = 1
while n < 6:
    try:
        num = int(input('input num: '))
    except:
        print('예외')
        continue

    nums.append(num)
    n += 1

print(f'nums : {nums}')