# OOP Lesson 2

class Wallet:
	
	def __init__(self, starting_amount):
		self.cash = starting_amount
		
	def spend(self, amount):
		new_amount = self.cash - amount
		print("Spending Money...")
		print("${} >> ${}".format(self.cash, new_amount))
		self.cash = new_amount

class SchoolSupply:
	
	def __init__(self, cost, wallet):
		self.cost = cost
		
		self.wallet = wallet
		
		self.wallet.spend(self.cost)
	
		
class Pencil (SchoolSupply):
	
	def __init__(self, wallet):
		super().__init__(1, wallet)
		
class Binder (SchoolSupply):
	
	def __init__(self, wallet):
		super().__init__(15, wallet)
		
	
	
my_wallet = Wallet(100)
Pencil(my_wallet)
Binder(my_wallet)
