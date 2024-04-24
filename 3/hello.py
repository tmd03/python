
class Human:
	def __init__(self):
		self.name="lucy"

	def hello(self):
		print(f'hi i am {self.name}')

class Man(Human):
	def __init__(self):
		self.name="hong"
	def pottery(self):
		print(f'{self.name} screaming!!')

class Woman(Human):
	def __init__(self, name:str,ddukbokiiCount:int):
		self.name=name
		self.dCnt = ddukbokiiCount
	def eatDDuk(self):
		self.dCnt = self.dCnt + 1
		print(f'{self.name} is eating ddukBokii.....')
	def scream(self):
		print(f'I eat {self.dCnt} ddukBokiis!!!!!')
	def hello(self):
		print(f'{self.name} says pottery is useless...')



theFirstHuman = Human()

theFirstHuman.hello()

hong = Man()

hong.hello()
hong.pottery()

han = Woman("han", 120)

han.hello()

han.scream()
han.eatDDuk()
han.scream()
