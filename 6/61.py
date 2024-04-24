# students = ['한혜승', '김소현', '이수윤', '함지수', '김성예']
#
# for i in range(5):
#     if i % 2 == 0 :
#         print('인덱스 짝수인 학생 : students[{}] : {}'.format(i, students[i]))
#     else:
#         print('인덱스 홀수인 학생 : students[{}] : {}'.format(i, students[i]))
#
#
# slength = len(students)
# # print(slength)
# #
# # for i in range(slength):
# #     print('i : {}'.format(i))
# #     print('students[{}] : {}'.format(i, students[i]))
#
# print('='*20)
# n = 0
# while n < slength :
#     print('i : {}'.format(n))
#     print('students[{}] : {}'.format(n, students[n]))
#     n += 1
#
# print('=' * 20)
# myfav = ['수영', '탁구', '농구','야구','축구']
#
# for i in range(len(myfav)):
#     print('myfavoriteSports[{}] : {}'. format(i, myfav[i]))
#
# print('=' * 20)
#
# for stu in students:
#     print(stu)

print('=' * 20)

stuCnts = [[1,18], [2,19], [3,23], [4,21], [5,20], [6,22], [7,17]]
total = 0

for classno, Cnts in stuCnts:
    print(f'{classno}반의 학생수 : {Cnts}')
    total += Cnts

average = int(total) // 7
print(f'평균학생수 = {average}')
print(f'전체학생수 = {total}')