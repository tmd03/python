students = ('지드래곤','태양','박명수','유재석','정준하')
for i in range(len(students)):
        print(f'n: {i}')
        print(f'students[{i}] : {students[i]}')
        i += 1

myfavN = (1,3,5,6,7)
friendfavN = (2,3,5,8,10)

print(f'myNumber: {myfavN}')
print(f'friendNumber: {friendfavN}')
for num in friendfavN:
    if num not in myfavN:
        myfavN = myfavN + (num, )

print(sorted(myfavN))
print('='*20)

scores = (9.5, 8.9, 9.2, 9.8, 8.8, 9.0)

scores = list(scores)
scores.sort()
print(scores)
scores.pop(0)
scores.pop(len(scores)-1)

print(scores)

for i in scores:
    print(i)