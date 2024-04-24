class NewPC:

    def __init__(self, name, cpu, memory, ssd):
        self.name = name
        self.cpu = cpu
        self.memory = memory
        self.ssd = ssd

    def doExcel(self):
        print('EXCEL RUN!')
    def doPhotoshop(self):
        print('PHOTOSHOP RUN!!')

    def printPCInfo(self):
        print(f'self.name: {self.name}')
        print(f'self.cpu: {self.cpu}')
        print(f'self.memory: {self.memory}')
        print(f'self.ssd: {self.ssd}')

myPC = NewPC('myPc', 'i5', '16', '256')
myPC.printPCInfo()
#=====================================

class Calculator:
    def __init__(self, number1, number2):
        self.number1 = 0
        self.number2 = 0
        self.result = 0

    def add(self):
        self.result = self.number1 + self.number2
        return self.result

    def sub(self):
        self.result = self.number1 - self.number2
        return self.result

    def mul(self):
        self.result = self.number1 * self.number2
        return self.result

    def div(self):
        self.result = self.number1 / self.number2
        return self.result
# def printPCInfo(self):
 #       print(f'self.name: {self.name}')
    def calNum(self):
        print(f'self.number1: {self.number1}')
        print(f'self.number2: {self.number2}')
        print(f'self.result: {self.result}')


calnewNum = Calculator(10, 20)
calnewNum.calNum()