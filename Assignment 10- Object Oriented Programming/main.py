# Elle Szabo
# ITP 115, Spring 2019
# Assignment 10
# eszabo@usc.edu
#ITP115_A10_Szabo_Elle.py

import csv

class Animal():
	def __init__(self, hunger = 0,  happiness = 0,  health = 0, energy = 0, age = 0, name= 0, species= 0):
		self.hunger = hunger
		self.happiness = happiness
		self.health = health
		self.energy = energy
		self.age = age
		self.name = name
		self.species = species
	def play(self):
		self.happiness += 10
		self.hunger += 5
	def feed(self):
		self.hunger += -10
	def giveMedicine(self):
		self.happiness += -20
		self.health += 20
	def sleep(self):
		self.energy += 20
		self.age += 1
	def _str_(self):
		string = "********************************\n"  + "Name: " + self.name + " the " + self.species + "\nHealth: " + str(self.health) + "\nHappiness: " + str(self.happiness) + "\nHunger: " + str(self.hunger)  + "\nEnergy: " + str(self.energy) + "\nAge: " + str(self.age)
		return string
	def checkValid(self):
		if self.hunger >100:
			self.hunger = 100
		elif self.hunger < 0:
			self.hunger = 0
		if self.happiness >100:
			self.happiness = 100
		elif self.happiness < 0:
			self.happiness = 0
		if self.health >100:
			self.health = 100
		elif self.health < 0:
			self.health = 0
		if self.energy >100:
			self.energy = 100
		elif self.energy < 0:
			self.energy = 0
		if self.age >100:
			self.age = 100
		elif self.age < 0:
			self.age = 0

def loadAnimals(fileName):
	openFile = open(fileName, "r")
	animalList = []
	for line in openFile:
		lineList = line.split(",")
		animal = Animal(int(lineList[0]), int(lineList[1]), int(lineList[2]), int(lineList[3]), int(lineList[4]), lineList[5], lineList[6])
		animalList.append(animal)
	return animalList
def displayMenu():
	print("1) Play")
	print("2) Feed")
	print("3) Give Medicine")
	print("4) Sleep")
	print("5) Print an Animal's stats")
	print("6) View All Animals")
	print("7) Exit\n")
def viewAll(animalList):
	for i in range(len(animalList)):
		print(animalList[i]._str_())
	print("\n********************************")
			
def selectAnimal(animalList):
	for i in range(len(animalList)):
		print(str(i+1) + ")", animalList[i].name, "the", animalList[i].species)
	max = len(animalList)
	selection = int(input("Please select an animal from the list (enter 1-" + str(max) + "): "))
	while selection > max or selection < 1:
		print("*Invalid selection, please try again.")
		selection = int(input("Please select an animal from the list (enter 1-" + str(max) + "): "))
	animal = animalList[selection-1]
	return animal
def writeFile(animalList):
	with open('animals.csv', mode = 'w') as animalFile:
		animalWriter = csv.writer(animalFile)
		for i in animalList:
			animalWriter.writerow([str(i.hunger)] + [str(i.happiness)] + [str(i.health)] + [str(i.energy)] + [str(i.age)]+[i.name]+[i.species])
def main():
	animalList = loadAnimals("animals.csv")
	select = 1
	print("Welcome to the Animal Daycare! Here is what we can do:\n")
	while select != 7:
		displayMenu()
		select = int(input("Please make a selection: "))
		while select >7 or select<1:
			print("*Invalid selection, please try again.\n")
			displayMenu()
			select = int(input("Please make a selection: "))
		if select >= 1 and select <=5:
			animal = selectAnimal(animalList)
			if select == 1:
				animal.play()
				animal.checkValid()
				print("You played with", animal.name, "the", animal.species + "!")
			if select == 2:
				animal.feed()
				animal.checkValid()
				print("You fed", animal.name, "the", animal.species + "!")
			if select == 3:
				animal.giveMedicine()
				animal.checkValid()
				print("You gave", animal.name, "the", animal.species, "some medicine!")
			if select == 4:
				animal.sleep()
				animal.checkValid()
				print(animal.name, "the", animal.species, "took a nap!")
			if select == 5:
				print(animal._str_())
				print("\n")
		elif select == 6:
			viewAll(animalList)
	writeFile(animalList)
	print("Data has been saved to the original file. Goodbye!")
main()
