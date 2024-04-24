scores = [int(input('국어 점수 입력: ')),
          int(input('영어 점수 입력: ')),
          int(input('수학 점수 입력: '))]

print(scores)

copyScores = scores.copy()

for idx, score in enumerate(copyScores):
    result = score * 1.1
    copyScores[idx] = 100 if result > 100 else result

print(f'이전 평균: {sum(scores / len(scores))}')
print(f'이후 평균: {sum(copyScores / len(copyScores))}')
