# OOP Lesson 1

from random import randint

##Object Oriented Programming

class Animal:
	
	def __init__(self, nickname):
		self.nickname = nickname
		self.health = 100
		self.food = 100
		
	def log(self, message):
		print("{}: {}".format(self.nickname, message))
		
	def print_info(self):
		message = "health: {}, food: {}".format(self.health, self.food)
		self.log(message)
		
	def heal(self):
		self.log("Healing...")
		self.food -= 10
		self.health += 5
		
	def play_russian_roulette(self):
		self.log("Playing Russian Roulette...")
		if randint(1, 3) == 2:
			self.log("Bang")
			self.health -= 50
		else:
			self.log("Click")
			
class Bear (Animal):
	def __init__ (self, nickname):
		super().__init__(nickname)
		
class SovietBear (Bear):
	def __init__(self, nickname):
		super().__init__(nickname)
	
	def play_russian_roulette(self):
		self.log("Playing Russian Roulette...")
		if randint(1, 7) == 1:
			self.log("Bang")
			self.health -= 50
		else:
			self.log("Click")
	
		
a = Animal("Paul")
a.print_info()
a.play_russian_roulette()
a.print_info()
a.heal()
a.print_info()

print("")

b = SovietBear("Finn")
b.print_info()
b.play_russian_roulette()
b.print_info()

#b = Animal()
