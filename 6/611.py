# studentinfo = {}
#
# studentinfo['name'] = input('이름 입력: ')
# studentinfo['age'] = input('나이 입력: ')
# studentinfo['mail'] = input('메일 입력: ')
#
# print(f'studentinfo : {studentinfo}')

print('='*20)
factorialDic = {}

for i in range(11):
    if i == 0 :
        factorialDic[i] = 1
    else:
        for j in range(1, (i+1)):
            factorialDic[i] = factorialDic[i-1] * j

print(f'factorialDic : {factorialDic}')

print('='*20)
mybodyinfo = {'name':'han', 'weight':83.0, 'height':1.8}
myBMI = mybodyinfo['weight'] / (mybodyinfo['height'] **2)
print(mybodyinfo)
print('%0.2f' %myBMI)

d = 0

for i in range(30):
    mybodyinfo['weight'] -= 0.3
    mybodyinfo['height'] += 0.001
    myBMI = mybodyinfo['weight'] / (mybodyinfo['height'] **2)

print(mybodyinfo)
print('%0.2f' %myBMI)

print('='*20)
min = 60
scores = {'kor':80, 'eng':50,'mat':86,'sci':45,'his':67}
fstr = 'F(재시험)'
fDic = {}

for key in scores:
    if scores[key] < min:
        scores[key] = fstr
        fDic[key] = fstr

print(f'scores: {scores}')
print(f'fDic: {fDic}')