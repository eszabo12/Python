from MenuItem import MenuItem
from Menu import Menu

class Diner():
	#creates a list of statuses to reference later
	STATUSES = ["seated", "ordering", "eating", "paying", "leaving"]
	def __init__(self, name):
		self.name = name
		self.order = []
		self.status = 0
	def getName(self):
		return self.name
	def getOrder(self):
		return self.order
	def getStatus(self):
		return self.status
	def setName(self, newName):
		self.name = newName
	def setOrder(self, newOrder):
		self.order = newOrder
	def setStatus(self, newStatus):
		self.status = newStatus
	def updateStatus(self):
		self.status += 1
	def addToOrder(self, objec):
		self.order.append(objec)
	def printOrder(self):
		print(self.name, "ordered:")
		for i in self.order:
			print(i)
	# no inputs, returns the cost of the meal
	def calculateMealCost(self):
		sum1 = 0
		for i in self.order:
			sum1 += i.price
		return sum1
	#prints out the diner information nicely
	def __str__(self):
		string = "Diner " + self.name + " is currently " + self.STATUSES[self.status] + "."
		return string
