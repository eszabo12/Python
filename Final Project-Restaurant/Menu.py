from MenuItem import MenuItem

class Menu():
	MENU_ITEM_TYPES = ["Drink", "Appetizer", "Entree", "Dessert"]
	def __init__(self, menuItemDictionary):
		# initializes the dictionary as an empty dictionary
		self.menuItemDictionary = {}
		dictionary = {}
		# opens  the csv file
		openFile = open(menuItemDictionary, "r")
		# loops through the file
		for line in openFile:
			# splits it up by commas
			lineList  = line.split(",")
			# creates menuitem objects based on the elements in the list
			objec = MenuItem(lineList[0], lineList[1], lineList[2], lineList[3])
			# creates a variable for the food type
			key = lineList[1]
			# checks if the key is already in the dictionary
			if key in self.menuItemDictionary.keys():
				# if it is, adds it to the list value
				self.menuItemDictionary[lineList[1]].append(objec)
			else:
				#if not, creates a new key-value pair
				self.menuItemDictionary[key] = [objec]
		openFile.close()
		'''
		kind of menu item, index in the value list
		returns: the item
		'''	
	def getMenuItem(self, kind, index):

		item = self.menuItemDictionary[kind][index]
		return item
		'''
		inputs: the kind of menu item
		returns: none
		'''	
	def printMenuItemsByType(self, kind):
		print(kind + "s:")
		for i in range(len(self.menuItemDictionary[kind])):
			print(i + ")", self.menuItemDictionary[kind][i])
		'''
		inputs: the kind of menu items
		returns: the number of menu items of that
		'''	
	def getNumMenuItemsByType(self, kind):
		length = len(self.menuItemDictionary[kind])
		return length
