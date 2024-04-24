class Tri:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def printTri(self):
        print(f'width: {self.width}')
        print(f'height: {self.height}')

    def printArea(self):
        return self.width * self.height / 2

class NewTri(Tri):
    def __init__(self, w, h):
        super().__init__(w, h)

    def printArea(self):
        return str(super().printArea())

ta = NewTri(7, 5)
ta.printArea()
trinangleArea = ta.printArea()
print(f'TriangleArea: {trinangleArea}')