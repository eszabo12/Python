import MusicLibraryHelper
import random
#shows the menu
def displayMenu():
	print("Welcome to your music library.")
	print("Options:")
	print("1) Display library")
	print("2) Display all artists")
	print("3) Add an album")
	print("4) Delete an album")
	print("5) Delete an artist")
	print("6) Search library")
	print("7) Generate a random playlist")
	print("8) Make your own playlist")
	print("9) Exit ")
# formats a given string so that the first letter is capitalized and the rest are lowercase
def formatString(artist):
		# splits it so that there can be multiple words in a string that each have this format
		format = artist.split()
		# loops through each word
		for i in range(len(format)):
			# makes them all lowercase and capitalizes them
			format[i] = format[i].lower()
			format[i] = format[i].capitalize()
		# after the loops is done, changes from list to string format again
		artist = " ".join(format)
		return artist
# creates a list verion of musicLibDictionary
def listDict(musicLibDictionary):
	# initializes empty string
	listDict = []
	# loops through the keys
	for key in musicLibDictionary.keys():
		# initializes empty lists each time so that the order is correct
		albumList = []
		artistList = []
		# puts the artist into the artist list
		artistList.append(key)
		# values are the list of all of the albums of a given artist
		values = musicLibDictionary[key]
		# loops through the albums and adds it to the album list
		for i in range(len(values)):
			albumList.append(values[i])
		# after each artist, adds their items to the entire list, separating each artist with a comma
		listDict += artistList + albumList + list(",")
	return listDict
# does the same thing with listDict except everything is in lowercase
def lowerDict(musicLibDictionary):
	lowerDict = []
	for key in musicLibDictionary.keys():
		albumList = []
		artistList = []
		# when it's added to the list it's lowercase
		artistList.append(key.lower())
		values = musicLibDictionary[key]
		for i in range(len(values)):
			albumList.append(values[i].lower())
		lowerDict += artistList + albumList + list(",")
	return lowerDict

def displayLibrary(musicLibDictionary):
	# if the library is empty, prints a message- for loop won't do anything if empty as well
	if not musicLibDictionary:
		print("Library empty.\n")
	for key in musicLibDictionary:
		print("Artist:", key)
		print("Albums:")
		# the values are all of the albums of a certain artist
		values = musicLibDictionary[key]
		# prints out all of the albums in a list
		for i in values:
			print("\t- ", i)
def displayArtists(musicLibDictionary):
	print("Displaying all artists:")
	# keys are artists
	for key in musicLibDictionary:
		print("\t- ", key)
def addAlbum(musicLibDictionary):
	artist = input("Enter artist: ")
	album = input("Enter album: ")
	# the artist input is formatted so that it's capitalized and the rest are lowercase
	# if the artist is in the key values, it's an existing artist
	if formatString(artist) in musicLibDictionary.keys():
		# if the artist exists but not the album, then it adds the album
		if not formatString(album) in musicLibDictionary[formatString(artist)]:
			musicLibDictionary[formatString(artist)].append(formatString(album))
	# if the artist doesn't exist, adds the artist and album to your library
	else:
		musicLibDictionary[artist] = []
		musicLibDictionary[artist].append(album)
def deleteAlbum(musicLibDictionary):
	artist = input("Enter artist: ")
	album = input("Enter album: ")
	artist = formatString(artist)
	album = formatString(album)
	# if the artist and album are in the library
	if artist in musicLibDictionary.keys() and album in musicLibDictionary[artist]:
		# if the artist has only one album
		if len(musicLibDictionary[artist]) == 1:
			# delete the artist and the album
			del musicLibDictionary[artist]
		# if the artist has more than one album, remove the album
		else:
			musicLibDictionary[artist].remove(album)
		return True
	else:
		return False
def deleteArtist(musicLibDictionary):
	artist = input("Enter artist: ")
	artist = formatString(artist)
	# if the artist exists
	if artist in musicLibDictionary.keys():
		# delete the artist
		del musicLibDictionary[artist]
		return True
	else:
		return False
def searchLibrary(musicLibDictionary):
	# creates a list of the music library entirely in lowercase
	lowerD = lowerDict(musicLibDictionary)
	# creates a list of the music library in its original case in order to access the correct capitalization
	listD = listDict(musicLibDictionary)
	#keyResults and valueResults are the hits that will be printed out to the reader
	#key is artist and value is album
	keyResults = []
	valueResults = []
	#a list of all of the albums in the library, in lowercase
	albumList = []
	# a list of all of the artists in the library, in lowercase
	artistList = []
	# loops through the dictionary
	for key in musicLibDictionary.keys():
		# adds to the artist list
		artistList.append(key.lower())
		values = musicLibDictionary[key]
		for i in range(len(values)):
			#adds the album to the album list by looping through the list albums from each artist
			albumList.append(values[i].lower())
	term = input("Please enter a search term: ")
	#loops through the lowercase dictionary
	for i in lowerD:
		# if the lowercased term is in the lowercase dictionary
		if term.lower() in i:
			#creates an index of where the term is in the lowercase dictionary
			index = lowerD.index(i)
			#final termn is the term in the original case dictionary- e.g. Beatles instead of beatles
			finalTerm  = listD[index]
			# loops through the artists
			for j in artistList:
				# if the lowercase term is in the artist list, then it adds it to the final artist results
				if finalTerm.lower() in j:
					keyResults.append(finalTerm)
			# same for the albums
			for k in albumList:
				if finalTerm.lower() in k:
					valueResults.append(finalTerm)
	# a function to print out the results of the search
	def printOut(valueResults):
		# if there are no results in a category
		if len(valueResults) == 0:
			print("No results")
		else:
			# loops through the list and adds formatting
			for i in valueResults:
				print("-", i)
	# prints out the results
	print("Artists containing '" + term + "':")
	printOut(keyResults)
	print("Albums containing '" + term + "':")
	printOut(valueResults)

def generateRandomPlaylist(musicLibDictionary):
	# intitalizes the playlist as a dictionary
	playlist = {}
	# loops through the library
	for key in musicLibDictionary.keys():
		# chooses a random album from this artist's albums
		choice = random.choice(musicLibDictionary[key])
		# adds the album to the playlist, using the artist as a key
		playlist[key] = choice
	print("Here is your random playlist: ")
	# loops through the playlist, printing out the value/album and the artist
	for key in playlist.keys():
		print("-", playlist[key], "by", key)

def generateCustomPlaylist(musicLibDictionary):
	# intitalizes a list of artists
	artists = []
	playlist = []
	# adds each artist to the list of artists
	for key in musicLibDictionary.keys():
		artists.append(key)
	cont = "y"
	while cont.lower() != "n":
		print("Your playlist so far:")
		# if the playlist is empty
		if len(playlist) == 0:
			print("Playlist empty.\n")
		# loops through the playlist if not empty
		for i in range(len(playlist)):
			# splits the item with a comma because the artist and album are separated with a comma
			# the first index holds the artist and the second holds the album
			item = playlist[i].split(",")
			# prints it out
			print("-", item[1], "by", item[0])
		#prints out all of the artists
		for i in range(len(artists)):
			print(str(i) + ")", artists[i])
		artistChoice = int(input("Select an artist from the list by entering its number: "))
		# error checks
		while artistChoice > len(artists)-1 or artistChoice < 0:
			print("*Error, please try again.")
			artistChoice = int(input("Select an artist from the list by entering its number: "))
		#creates a string variable for the artist instead of an integer-- e.g. "Beatles"
		string1 = artists[artistChoice]
		# adds the artist to the playlist
		playlist.append(string1)
		#finds the index in the playlist of the artist
		index = playlist.index(string1)
		#creates a variable for all of the albums of the given artist
		albums = musicLibDictionary[string1]
		for i in range(len(albums)):
			print(str(i) + ")", albums[i])
		albumChoice = int(input("Select an album from the list by entering its number: "))
		#error checks
		while albumChoice > len(albums)-1 or albumChoice < 0:
			print("*Error, please try again.")
			albumChoice = int(input("Select an album from the list by entering its number: "))
		# changes the element of the playlist that used to contain just the artist and now puts in the artist and album
		playlist[index] = playlist[index] + "," + albums[albumChoice]
		cont = input("Would you like to continue building your playlist? (y/n) ")
		while cont.lower() != "y" and cont.lower() != "n":
			print("*Error, please try again.")
def main():
	# loads the music library
	musicLibDictionary = MusicLibraryHelper.loadLibrary('musicLibrary.dat')
	choice = 1
	while choice != 9:
		displayMenu()
		choice = int(input())
		while choice > 9 or choice < 0:
			print("*Error, please try again.")
			displayMenu()
			choice = int(input())
		if choice == 1:
			displayLibrary(musicLibDictionary)
		elif choice == 2:
			displayArtists(musicLibDictionary)
		elif choice == 3:
			addAlbum(musicLibDictionary)
		elif choice == 4:
			if deleteAlbum(musicLibDictionary):
				print("Delete album success!")
			else:
				print("Delete album failed.")
		elif choice == 5:
			if deleteArtist(musicLibDictionary):
				print("Delete artist success!")
			else:
				print("Delete artist failed.")
		elif choice == 6:
			searchLibrary(musicLibDictionary)
		elif choice == 7:
			generateRandomPlaylist(musicLibDictionary)
		elif choice == 8:
			generateCustomPlaylist(musicLibDictionary)
	# saves the file again
	print("Saving music library...")
	MusicLibraryHelper.saveLibrary('musicLibrary.dat', musicLibDictionary)
	print("Goodbye!")
main()
