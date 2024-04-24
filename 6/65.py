scores = [[1,9.5],[2,8.9],[3,9.2],[4,9.8],[5,8.8],[6,9.0]]
high = max(scores, key=lambda x:x[1])[1]
low = min(scores, key=lambda x:x[1])[1]

for idx, value in scores:
    if value == high:
        print(f'maxScore:{value}, maxScoreIdx:{idx-1}')
    elif value == low:
        print(f'minScore:{value}, minScoreIdx:{idx-1}')

print('='*20)

mylist = ['마케팅 회의','회의록 정리','점심 약속','월간 업무 보고','치과 방문','마트 장보기']
print(mylist)
inputN = input('삭제할 일정 입력: ')

while inputN in mylist:
    mylist.remove(inputN)
    print(mylist)
else:
    print('그런 일정은 없는디....')


