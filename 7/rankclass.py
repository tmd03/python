class rankdeviation:
    def __init__(self, ms, fs):
        self.m_score = ms
        self.f_score = fs
        self.m_ranks = [0 for i in range(20)]
        self.f_ranks = [0 for i in range(20)]
        self.ranks = [0 for i in range(20)]

    def setRank(self, s):
        ranks = [0 for i in range(20)]
        for idx, num1 in enumerate(s):
            for num2 in s:
                if num1 < num2:
                    ranks[idx] += 1
        return ranks
    def setMidRank(self):
        self.m_ranks = self.setRank(self.m_score)
    def getMidRank(self):
        return self.m_ranks

    def setEndRank(self):
        self.f_ranks = self.setRank(self.f_score)
    def getEndRank(self):
        return self.f_ranks

    def printRank(self):
        for idx, mRank in enumerate(self.m_ranks):
            deviation = mRank - self.f_ranks[idx]

            if deviation > 0:
                deviation = '↓' + str(abs(deviation))
            elif deviation < 0:
                deviation = '↑' + str(abs(deviation))
            elif deviation == 0:
                deviation = '=' + str(abs(deviation))

            print(f'midrank: {mRank} \t endrank: {self.f_ranks[idx]} \t Deviation: {deviation}')

import random

m_score = random.sample(range(50,101),20)
f_score = random.sample(range(50,101),20)

rd = rankdeviation(m_score, f_score)
rd.setMidRank()
print(f'midScores: {m_score}')
print(f'midRanks: {rd.getMidRank()}')
rd.setEndRank()
print(f'endScores: {f_score}')
print(f'endRanks: {rd.getEndRank()}')
rd.printRank()

print('hi yo')