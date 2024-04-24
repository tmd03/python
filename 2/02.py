import random

sum = 0
date = 1
flag = True

while flag:
    patient = random.randint(50, 100)
    sum += patient
    date += 1
    print('날짜 : {}, /t 오늘 환자수, /t 누적환자수 : {}'.format(date, patient, sum))

    if sum >= 10000:
        flag = False