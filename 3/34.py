class MidExam:
    def __init__(self, s1, s2, s3):
        print('[MidExam] __init__()')

        self.mid_kor = s1
        self.mid_eng = s2
        self.mid_mat = s3

    def printScores(self):
        print(f'mid_kor = {self.mid_kor}')
        print(f'mid_eng = {self.mid_eng}')
        print(f'mid_mat = {self.mid_mat}')

class EndExam(MidExam):
    def __init__(self, s1, s2, s3, s4, s5, s6):
        print('[EndExam] __init__()')

        super().__init__(s1, s2, s3)

        self.end_kor = s4
        self.end_eng = s5
        self.end_mat = s6

    def printScores(self):
        print(f'end_kor = {self.end_kor}')
        print(f'end_eng = {self.end_eng}')
        print(f'end_mat = {self.end_mat}')

    def totalScores(self):
        total = self.mid_kor + self.mid_eng + self.mid_mat
        total += self.end_kor + self.end_eng + self.end_mat

        return total

    def averageScores(self):

        return self.totalScores() / 6

sco = EndExam(98, 95, 65, 76, 86, 98)
sco.totalScores()
sco.averageScores()

print(f'total : {sco.totalScores()}')
print(f'average: {sco.averageScores()}')
