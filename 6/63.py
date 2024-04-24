# cars = ['그랜저', '소나타','말리부','카니발','쏘렌토']
#
# n = 0
#
# while n < len(cars):
#     print(cars[n])
#     n += 1
#
# print('='*20)
#
# n = 0
# flag = True
# while flag:
#     print(cars[n])
#     n += 1
#
#     if n == len(cars):
#         flag = False
#
# print('='*20)
# stuCnts = [[1,19],[2,20],[3,22],[4,18],[5,21]]
# n = 0
# while n < len(stuCnts):
#     print('{}학급 학생수: {}'.format(stuCnts[n][0], stuCnts[n][1]))
#     n += 1

print('=' * 20)
stuCounts = [[1,18], [2,19], [3,23], [4,21], [5,20], [6,22], [7,17]]
total = 0
avg = 0
n = 0
while n < len(stuCounts):
    print('{}학급 학생수: {}'.format(stuCounts[n][0], stuCounts[n][1]))

    total += stuCounts[n][1]
    n += 1

avg = total / len(stuCounts)

print(f'평균학생수 = {avg}')
print(f'전체학생수 = {total}')






