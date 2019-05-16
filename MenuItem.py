
class MenuItem():
	#inputs: the name, type, price, and description of the dish
	# return: none
	def __init__(self, name, kind, price, description):
		self.name = name
		self.kind = kind
		self.price = float(price)
		self.description = description
		'''
		inputs: none
		returns: a string
		'''
	def __str__(self):
		string = self.name + " (" + self.kind + "): $" + str(self.price) + "\n\t" + self.description
		return string	
	def getName(self):
		return self.name
	def getType(self):
		return self.kind
	def getPrice(self):
		return self.price
	def getDescription(self):
		return self.description
		'''
		inputs: new name
		returns: none
		'''
	def setName(self, newName):
		self.name = newName
		'''
		inputs: new type
		returns: none
		'''	
	def setType(self, newType):
		self.kind = newType
		'''
		inputs: new price
		returns: none
		'''	
	def setPrice(self, newPrice):
		self.price = newPrice
		'''
		inputs: new description
		returns: none
		'''	
	def setDescription(self, newDescription):
		self.description = newDescription