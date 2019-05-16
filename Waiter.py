from Menu import Menu
from Diner import Diner

class Waiter():
	def __init__(self, menu):
		# sets it to an empty list
		self.diners = []
		self.menu = menu
	# adds a diner to the list
	def addDiner(self, diner):
		self.diners.append(diner)
	#finds how many diners there are
		'''
		inputs: none
		returns: number of diners
		'''	
	def getNumDiners(self):
		length = len(self.diners)
		return length
		'''
		inputs: none
		returns: none
		'''	
	def printDinerStatuses(self):
		STATUSES = ["seated", "ordering", "eating", "paying", "leaving"]
		for stat in STATUSES:
			print("Diners who are currently", stat + ":")
			for diner in self.diners:
				if diner.STATUSES[diner.status] == stat:
					print("\t" + str(diner))
	# if the diner's status. parameters: none. returns: none.
	def takeOrders(self):
		#loops through all of the diners
		for diner in self.diners:
			# checks if the diner's status is 1, meaning they're ordering
			if diner.status == 1:
				#loops through the menu keys
				print("\n")
				for j in self.menu.menuItemDictionary.keys():
					print("\n-----" + j + "s-----")
					#loops though all of the menu items in each key(category)
					for k in range(len(self.menu.menuItemDictionary[j])):
					#prints a numbered list and description of the menu item accessing the __str__ method
						print(str(k) + ") " + str(self.menu.menuItemDictionary[j][k]))
				# after the menu items in each category are  printed out, it asks the user for input
					request = int(input(diner.name + ", please select a " + j + " menu item number.\n"))
					#error checks
					count = 0
					for item in self.menu.menuItemDictionary[j]:
						count += 1
					while request > count-1 or request < 0:
						request = int(input())
					menuitem = self.menu.menuItemDictionary[j][request]
					diner.order.append(menuitem)
				#prints out the diner's order
				print(diner.name, "ordered:")
				for i in diner.order:
					print("-", i)
	# no inputs or return values
	def ringUpDiners(self):
		for diner in self.diners:
			# checks if the diner's status is 3, meaning they're paying
			if diner.status == 3:
				cost = diner.calculateMealCost()
				print("\n" + diner.name + ", your meal cost $"+ str(round(cost, 2))+ ".")
	# no inputs or return values
	def removeDoneDiners(self):
		for diner in self.diners:
			if diner.status == 4:
				print("\n" + diner.name + ", thank you for dining with us! Come again soon!")
		for i in reversed(range(len(self.diners))):
			if self.diners[i].status == 4:
				del self.diners[i]
	# no inputs or return values
	def advanceDiners(self):
		self.printDinerStatuses()
		self.takeOrders()
		self.ringUpDiners()
		self.removeDoneDiners()
		#advances all the diners
		for diner in self.diners:
			diner.updateStatus()