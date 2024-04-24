# min = 60
# # scores = ('국어',58),('영어',77),('수학',89),('과학',99),('국사',50)
# #
# # n = 0
# # while n < len(scores):
# #     if scores[n][1] < min :
# #         print(f'과락과목: {scores[n][0]}, 점수: {scores[n][1]}')
# #
# #     n += 1
#
#
# kor = int(input('국어 점수: '))
# eng = int(input('영어 점수: '))
# mat = int(input('수학 점수: '))
# sci = int(input('과학 점수: '))
# his = int(input('역사 점수: '))
#
# scores = ('국어', kor),('영어', eng),('수학', mat),('과학', sci),('역사', his)
#
# n = 0
# while n < len(scores):
#     if scores[n][1] < min:
#         print(f'과락과목: {scores[n][0]}, 점수: {scores[n][1]}')

    # n += 1

print('='*20)
stuCnts = (1,18), (2,19), (3,23), (4,21), (5,20), (6,22), (7,17)

mincnt = 0 ; minclass = 0
maxcnt = 0 ; maxclass = 0

n = 0

while n < len(stuCnts):

    if mincnt == 0 or mincnt > stuCnts[n][1]:
        minclass = stuCnts[n][0]
        mincnt = stuCnts[n][1]

    if maxcnt < stuCnts[n][1]:
        maxclass = stuCnts[n][0]
        maxcnt = stuCnts[n][1]

    n += 1

print(f'학생 수가 가장 작은 반 : {minclass}반({mincnt}명)')
print(f'학생 수가 가장 많은 반 : {maxclass}반({maxcnt}명)')