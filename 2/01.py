mintem = int(input('최저 기온 입력 :'))
maxtem = int(input('최고 기온 입력 :'))

result = int(maxtem - mintem)

if result >= 11:
    print('일교차:{}'.format(result))
    print('감기조심')
else :
    print('일교차:{}'.format(result))
    print('산책하기 딱좋아')