myN = [1,3,5,6,7]
friendN = [2,3,5,8,10]

print(f'myfavoriteNumber: {myN}')
print(f'friendfavoriteNumber: {friendN}')
addlist = myN + friendN
print(f'addlist : {addlist}')
result = []
for num in addlist:
    if num not in result:
        result.append(num)
        result.sort()
print(f'result : {result}')

print('='*20)
scores = [9.5,8.9,9.2,9.8,8.8,9.0]
print(f'player score : {scores}')

scores.sort()
print(f'player score : {scores}')
scores.pop(0)
scores.pop(len(scores)-1)
print(f'player score : {scores}')

avg = 0
total = 0
for score in scores:
    total += score
avg = total / len(scores)

print('총점 : %.2f' %total)
print('평균 : %.2f' %avg)

print('='*20)
secret = '27156231'
secretlist = []

for x in secret:
    secretlist.append(int(x))

secretlist.reverse()
print(secretlist)

p = secretlist[0] * secretlist[1]
secretlist.insert(2, p)
p = secretlist[3] * secretlist[4]
secretlist.insert(5, p)
p = secretlist[6] * secretlist[7]
secretlist.insert(8, p)
p = secretlist[9] * secretlist[10]
secretlist.insert(11, p)
print(secretlist)

print('='*20)
import random

samplelist = random.sample(range(1,11),10)
inputN = int(input('숫자 7의 위치 입력: '))
if inputN == samplelist[0]:
    print('당첨!!!!')
else:
    print('탈락ㅠㅠ')
print(samplelist)
searchIdx = samplelist.index(7)
print('serchIdx : {}'.format(searchIdx))


print('='*20)
import random
types = ['A', 'B', 'O', 'AB']
typeCnt = []
todayData = []

for i in range(100):
    type = types[random.randrange(len(types))]
    todayData.append(type)

print(f'today Data : {todayData}')
print(f'today Data length : {len(todayData)}')

for type in types:
    print('{}형 \t: {}개'.format(type,todayData.count(type)))