# Elle Szabo
# ITP 115, Spring 2019
# Assignment 8
# eszabo@usc.edu

# Writes the data to a file
def writeFile(fileName, resultsName, carListMin, carListMax, whichYear):
	fileIn = open(fileName, "r")
	min = 400
	# Finds the minimum mpg
	for line in fileIn:
		line = line.strip()
		dataList = line.split(",")
		if dataList[0] != "CLASS":
			if int(dataList[8]) < min:
				min = int(dataList[8])
	# Finds the max mpg
	max = -5
	fileIn.close()
	fileIn = open(fileName, "r")
	for line in fileIn:
		line = line.strip()
		dataList = line.split(",")
		if dataList[0] != "CLASS":
			if int(dataList[8]) > max:
				max = int(dataList[8])
	fileIn.close()
	# Opens a new file and prints all of the information to it
	fileNew = open(resultsName, "w")
	print("EPA City MPG Calculator (" + str(whichYear) + ")", file=fileNew)
	print("\n---------------------------------\n", file =fileNew)
	print("Maximum Mileage (city):", str(max), file =fileNew)
	# Loops through the list of cars
	for i in carListMax:
		print("\t" + i, file=fileNew)
	print("Minimum Mileage (city):", str(min), file=fileNew)
	for i in carListMin:
		print("\t" + i, file=fileNew)
	fileNew.close()

def findCarListMax(whichYear):
	carListMax = []
	# finds the file from the year given
	fileName = "epaVehicleData" + str(whichYear) + ".csv"
	fileIn = open(fileName, "r")
	#finds the true maximum mpg
	max = -5
	for line in fileIn:
		line = line.strip()
		dataList = line.split(",")
		if dataList[0] != "CLASS":
			if int(dataList[8]) > max:
				max = int(dataList[8])
	fileIn.close()
	# loops through and adds the car to a list if it has the max mpg
	fileIn = open(fileName, "r")
	for line in fileIn:
		line = line.strip()
		dataList = line.split(",")
		if dataList[0] != "CLASS":
			if not ("VAN" in dataList[0]) and not ("TRUCK" in dataList[0]):
				if int(dataList[8]) == max:
					addition = dataList[1] + " " + dataList[2]
					carListMax.append(addition)
	fileIn.close()
	return carListMax
	
def findCarListMin(whichYear):
	carListMin = []
	fileName = "epaVehicleData" + str(whichYear) + ".csv"
	fileIn = open(fileName, "r")
	# Finds the true minumum
	min = 400
	for line in fileIn:
		line = line.strip()
		dataList = line.split(",")
		if dataList[0] != "CLASS":
			if int(dataList[8]) < min:
				min = int(dataList[8])
	fileIn.close()
	fileIn = open(fileName, "r")
	# loops through and adds the car to a list if it has the min mpg
	for line in fileIn:
		line = line.strip()
		dataList = line.split(",")
		if dataList[0] != "CLASS":
			if not ("VAN" in dataList[0]) and not ("TRUCK" in dataList[0]):
				if int(dataList[8]) == min:
					addition = dataList[1] + " " + dataList[2]
					carListMin.append(addition)
	fileIn.close()
	return carListMin
# Sees if the car type is valid for the extra credit
def isTypeInList(whichYear, carType):
	fileName = "epaVehicleData" + str(whichYear) + ".csv"
	fileIn = open(fileName, "r")
	count = 0
	for line in fileIn:
		line = line.strip()
		dataList = line.split(",")
		if dataList[0] == carType:
			count += 1
	fileIn.close()
	if count == 1:
		return True
	else:
		return False
def main():
	whichYear = int(input("Which year would you like to select? (2008 or 2009) "))
	# Error checks for input
	while whichYear != 2008 and whichYear != 2009:
		print("*Invalid input, please try again!")
		whichYear = input("Which year would you like to select? (2008 or 2009) ")
	resultsName = input("Enter the filename to save results to: ")
	# finds the file name from the given year
	fileName = "epaVehicleData" + str(whichYear) + ".csv"
	# assigns the variables using the functions
	carListMin = findCarListMin(whichYear)
	carListMax = findCarListMax(whichYear)
	#writes it all to a new file
	writeFile(fileName, resultsName, carListMin, carListMax, whichYear)
	print("Operation Success! Mileage data has been saved to", resultsName)
	# The extra credit option
	otherCars = input("Would you see mileage for other cars? (y/n)")
	# error checks for invalid answers
	while otherCars.lower() != "y" and otherCars.lower() != "n":
		print("Invalid input, please try again!")
		otherCars = input("Whould you see mileage for other cars? (y/n)")
	if otherCars.lower() == "y":
		carType = input("What car type would you like to see? Type in the format: \"Midsize cars\" ")
		carType = carType.lower()
		# Error checks to see if the type is valid
		while not isTypeInList(whichYear, carType):
			print("Invalid type, please try again!")
			carType = input("What car type would you like to see? Type in the format: \"Midsize cars\" ")
			carType = carType.lower()
		# Finds the file from the year
		fileName = "epaVehicleData" + str(whichYear) + ".csv"
		fileIn = open(fileName, "r")
		carListMin = []
		fileName = "epaVehicleData" + str(whichYear) + ".csv"
		fileIn = open(fileName, "r")
		# Finds the minimum of that car type
		min = 400
		for line in fileIn:
			line = line.strip()
			dataList = line.split(",")
			if dataList[0] == carType:
				if int(dataList[8]) < min:
					min = int(dataList[8])
		fileIn.close()
		# Finds the max of that car type
		fileIn = open(fileName, "r")
		for line in fileIn:
			line = line.strip()
			dataList = line.split(",")
			if dataList[0] != "CLASS":
				if dataList[0] == carType:
					if int(dataList[8]) == min:
						addition = dataList[1] + " " + dataList[2]
						# creates the list of cars with the minimum mpg
						carListMin.append(addition)
		fileIn.close()
		carListMax = []
		fileIn = open(fileName, "r")
		max = -5
		for line in fileIn:
			line = line.strip()
			dataList = line.split(",")
			if dataList[0] == carType:
				if int(dataList[8]) > max:
					max = int(dataList[8])
		fileIn.close()
		fileIn = open(fileName, "r")
		for line in fileIn:
			line = line.strip()
			dataList = line.split(",")
			if dataList[0] != "CLASS":
				if not ("VAN" in dataList[0]) and not ("TRUCK" in dataList[0]):
					if int(dataList[8]) == max:
						addition = dataList[1] + " " + dataList[2]
						carListMax.append(addition)
		fileIn.close()
		# Writes the other data to a file
		resultsName = input("Enter the filename to save results to: ")
		fileNew = open(resultsName, "w")
		print("EPA City MPG Calculator (" + str(whichYear) + ")", file=fileNew)
		print("\n---------------------------------\n", file =fileNew)
		print("Maximum Mileage (city):", str(max), file =fileNew)
		# Loops through the list of cars
		for i in carListMax:
			print("\t" + i, file=fileNew)
		print("Minimum Mileage (city):", str(min), file=fileNew)
		for i in carListMin:
			print("\t" + i, file=fileNew)
		fileNew.close()
		print("Operation Success! Mileage data for the specified type of car has been saved to", resultsName)
	print("Thanks, and have a great day!")
main()
