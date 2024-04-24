# min = 60
# scores = [['국어', 58],['영어', 77],['수학',89],['과학',99],['국사',50]]
#
# for sub, score in scores: #1
#     if score < min:
#         print(f'과락 과목:{sub}, 점수:{score}')
#
# for item in scores: #2
#     if item[1] < min:
#         print(f'과락 과목:{sub}, 점수:{score}')
#
# kor = int(input('국어 점수:'))
# eng = int(input('영어 점수:'))
# mat = int(input('수학 점수:'))
# sci = int(input('과학 점수:'))
# his = int(input('국사 점수:'))
#
# scores = [['국어', kor],['영어', eng],['수학',mat],['과학',sci],['국사',his]]
#
# for item in scores: #2
#      if item[1] < min:
#          print(f'과락 과목:{item[0]}, 점수:{item[1]}')



stuCnt = [[1, 18],[2,19],[3,23],[4,21],[5,20],[6,22],[7,17]]
min_stu = min(stuCnt, key=lambda x:x[1])[1]
max_stu = max(stuCnt, key=lambda x:x[1])[1]


for item in stuCnt:
    if item[1] == min_stu:
        print(f'학생 수가 가장 적은 학급(학생수):{item[0]}반({item[1]}명)')
    elif item[1] == max_stu:
        print(f'학생 수가 가장 많은 학급(학생수):{item[0]}반({item[1]}명)')