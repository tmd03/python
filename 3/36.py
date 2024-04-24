from abc import ABCMeta
from abc import abstractmethod

class Airplane(metaclass=ABCMeta):
    @abstractmethod #추상클래스란 맞는데다 갖다써라는 뜻
    def flight(self):
        pass

    def forward(self):
        print('전진!!')
    def backward(self):
        print('후진!!')

class Airliner(Airplane):
    def __init__(self, c):
        self.color = c

    def flight(self):
        print('시속 400')

class fighterplane(Airplane):
    def __init__(self, c):
        self.color = c

    def flight(self):
        print('시속 700')


al = Airliner('red')
al.flight()
al.forward()
al.backward()
fl = fighterplane('blue')
fl.flight()
fl.forward()
fl.backward()