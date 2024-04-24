min = 60
scores = [['국어', 58],['영어', 77],['수학',89],['과학',99],['국사',50]]

n = 0
while n < len(scores):
    sub = scores[n][0]
    score = scores[n][1]
    if score < min :
        print('과락 과목: {}, 점수: {}'.format(sub, score))
    n += 1

print('='*20)
str = 'hello python!'
for idx, value in enumerate(str):
    print(f'{idx}:{value}')

print('='*20)
sports = ['농구','야구','축구','테니스','수영']
for idx, value in enumerate(sports):
    print(f'{idx}:{value}')

print('='*20)
fvrspts = input('가장 좋아하는 스포츠 입력: ')
bestspt = 0

for idx, value in enumerate(sports):
    if value == fvrspts:
        bestspt += idx + 1

print('{}(은)는 {}번째에 있습니다.'.format(fvrspts, bestspt))

print('='*20)
numbers = [1, 3, 6, 11, 45, 54, 62, 74, 85]
inputnum = int(input('숫자 입력: '))
insertidx = 0

for idx, num in enumerate(numbers):
    print(idx, num)

    if insertidx == 0 and inputnum < num:
        insertidx = idx

numbers.insert(insertidx, inputnum)
print(numbers)

