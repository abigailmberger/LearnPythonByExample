# Open the file: Open is a function that opens a file and returns a FileObject
# Create variable for the file
# First argument is the file name of the file that you are opening
# Second argument is the file mode
#	r - read only
#	r+ - read and write
#	w - write only (BE CAREFUL)
#	a - append
fileToOpen = open("dataFileExamplesGitHubExplain.txt", "r")

# You can read a file as a string or a list, so this program gives the
# the user a choice
howToRead = input("Read as a string or a list? ")


if howToRead == "string" :
	
	# Returns the entire file as one big string
	contents = fileToOpen.read()
	
	print(contents)


elif howToRead == "list" :

	# The easiest way to print as a list leaves blank line '\n' in the text
	# between the items, so it depends how you want it to look when its printed
	# This code gies the user a choice
	
	# Returns a list, with each line of the file is one item
	contents = fileToOpen.readlines()
	print(contents)

	
# Always need to close the file
# May corrupt file if you do not close
fileToOpen.close()



# ------------------------ Exercises -------------------------

# 1. Rewrite the open function to ask the user which file to open using a variable
#
# 2. Read the file as a list and use the functions from the previous unit 
# 		to add to or delete items from the list that is printed in terminal
#
# 3. In order to remove the blank line \n left when reading into a list, you can use
# 		contents = fileToOpen.read().splitlines()
#		for line in contents:
#			print(line)
# 	Add the if statement to ask the user which way they want the list to print

