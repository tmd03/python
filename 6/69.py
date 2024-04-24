# min = 60
# scores = ('국어',58),('영어',77),('수학',89),('과학',99),('국사',50)
#
# # for sub, score in scores:
# #     if score < min:
# #         print(f'과락 과목:{sub}, 점수:{score}')
#
# for item in scores:
#     if item[1] < min:
#         print(f'과락 과목:{item[0]}, 점수:{item[1]}')
print('='*20)

stuCnts = (1,18), (2,19), (3,23), (4,21), (5,20), (6,22), (7,17)

# maxclass = 0 ; minclass = 0
# maxcnt = 0; mincnt = 0
#
# for classn, cnt in stuCnts:
#     if mincnt == 0 or mincnt > cnt :
# #         minclass = classn
# #         mincnt = cnt
# #
# #     if maxcnt < cnt:
# #         maxclass = classn
# #         maxcnt = cnt
#
# print(f'학생수가 가장 적은 학급(학생수): {minclass}반({mincnt})')
# print(f'학생수가 가장 많은 학급(학생수): {maxclass}반({maxcnt})')

n = 0
total = 0
avg = 0

while n < len(stuCnts):
    print(f'{stuCnts[n][0]}반 학생 수 : {stuCnts[n][1]}명')
    classno = stuCnts[n][0]
    cnt = stuCnts[n][1]

    n += 1
    total += cnt

print(total)
print(total / len(stuCnts))




