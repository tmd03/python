uri = 'C:/pythontxt/'

import random

def writeNumbers(n):
    for idx, num in enumerate(n):
        with open(uri + 'lotto.txt', 'w')as f:
            if idx < (len(n) - 2):
                f.write(str(num) + ', ')
            elif idx == (len(n) - 2):
                f.write(str(num))
            elif idx == (len(n) - 1):
                f.write("\n")
                f.write('bonus: ' + str(num))
                f.write('\n')

rn = random.sample(range(1,46), 7)
print(f'rNums: {rn}')

writeNumbers(rn)


