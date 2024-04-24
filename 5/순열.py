# inputN = int(input('n 입력: '))
# inputR = int(input('r 입력: '))
# result = 1
#
# for n in range(inputN, inputN-inputR, -1):
#     print('n : {}'.format(n))
#     result = result * n
#
# print(f'result: {result}')

#======================================

friend = int(input('친구 수 : '))
result = 1

for n in range(1, friend):
    result *= n
    # 팩토리얼이랑 똑같음

print(f'result : {result}')