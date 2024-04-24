students = ('지드래곤','태양','박명수','유재석','정준하')

for stu in range(5):
    if stu % 2 == 0:
        print('--인덱스가 짝수인 학생--')
        print(f'students[{stu}] : {students[stu]}')
    else:
        print('--인덱스가 홀수인 학생--')
        print(f'students[{stu}] : {students[stu]}')

print('='*20)
searchName = input('학생 이름 입력: ')
if searchName in students:
    print(f'{searchName} 학생은 우리반입니다')
else:
    print(f'{searchName} 학생은 나가!!!!')

print('='*20)
import random

inputN = int(input('숫자 입력(확률 50%): '))
randomTuple = random.sample(range(1,10),5)

if inputN in randomTuple:
    print('빙고!')
else:
    print('다음기회에~')
print(randomTuple)
print(f'userNumber: {inputN}')
