#!/usr/bin/python
# -*- coding: utf-8 -*-


# import only system from os 
from os import system, name

# import sleep to show output for some time period 
from time import sleep

# define our clear function 
def clear(): 
	_ = system('clear') 

# define list print function
def printList(inp):
	clear()
	for i in range(len(inp)):
		# automatic indenting so it all lines up and looks pretty
		numStr = str(i + 1)
		if len(inp) > 9 and i < 9:
			numStr = numStr + " "
		if len(inp) > 99 and i < 99:
			numStr = numStr + " "

		# translate 0 and 1 into readable text
		if inp[i][0] == True:
			lockState = "Locked"
		else:
			lockState = "Unlocked"

		if inp[i][1] == True:
			openState = "Closed"
		else:
			openState = "Open"

		print(numStr + ' ' + "[" + lockState + ", " + openState + ", " + str(inp[i][2]) + ", " + str(inp[i][3]) + ", " + str(inp[i][4]) + "]")
	raw_input("Press Enter To Continue")
	clear()


# draw out a pretty looking cabinet so we can see with our human eyes
def visualize(inp):
	for i in range(5):
		stringList = [
			"_",
			"⎸",
			"⎸",
			"⎸",
			"‾"
		]
		for i2 in range(4):
			# calculate drawer number and indentation
			drawerNum = (i * 4) + i2
			numString = str(drawerNum + 1)
			if drawerNum < 9:
				numString = " " + numString

			# default locked
			lockIcon = "X"
			if drawers[drawerNum][0] == False:
				lockIcon = "O"

			# default closed
			closeIcon = "-"
			if drawers[drawerNum][1] == False:
				closeIcon = "/"

			# add all the strings where they need to go
			stringList[0] += "_______"
			stringList[1] += " " + numString + "   ⎸"
			stringList[2] += "  " + lockIcon + "   ⎸"
			stringList[3] += "  " + closeIcon + "   ⎸"
			stringList[4] += "‾‾‾‾‾‾‾"
		for i2 in range(5):
			print(stringList[i2])

'''
X = locked
O = unlocked

- = closed
/ = open
____________________________
⎸  1   ⎸  2   ⎸  3   ⎸  4   ⎸
⎸  X   ⎸  O   ⎸  X   ⎸  X   ⎸
⎸  -   ⎸  -   ⎸  /   ⎸  /   ⎸
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
____________________________
⎸  5   ⎸  6   ⎸  7   ⎸  8   ⎸
⎸  X   ⎸  X   ⎸  X   ⎸  O   ⎸
⎸  -   ⎸  -   ⎸  -   ⎸  -   ⎸
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
____________________________
⎸  9   ⎸ 10   ⎸ 11   ⎸ 12   ⎸
⎸  O   ⎸  X   ⎸  X   ⎸  X   ⎸
⎸  /   ⎸  -   ⎸  -   ⎸  /   ⎸
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
____________________________
⎸ 13   ⎸ 14   ⎸ 15   ⎸ 16   ⎸
⎸  X   ⎸  X   ⎸  X   ⎸  X   ⎸
⎸  -   ⎸  -   ⎸  /   ⎸  -   ⎸
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
____________________________
⎸ 17   ⎸ 18   ⎸ 19   ⎸ 20   ⎸
⎸  X   ⎸  X   ⎸  O   ⎸  X   ⎸
⎸  -   ⎸  -   ⎸  -   ⎸  -   ⎸
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
'''

# start with blank screen
clear()

# main data structure
# 0: locked/unlocked status, true = locked, false = unlocked
# 1: closed/open status, true = closed, false = open
# 2: Username, None = no user
# 3: Password, None = no user
# 4: Flag, True = drawer is reserved, False = drawer is not reserved
drawers = [	
]

# populate the list
for i in range(20):
	drawers.append([
		True,
		True,
		None,
		None,
		False
	])

while True:
	visualize(drawers)
	action = raw_input("Type Your Action:\n")
	if action == "print list":
		printList(drawers)
	elif action[:4] == "open":
		# number parsing
		drawerToOpen = ""
		# length will be 6 if single digit, 7 if double digit
		if len(action) == 7:
			drawerToOpen = int(action[-2:]) # slicing magic
		else:
			drawerToOpen = int(action[-1:]) # slicing magic
		drawerToOpen -= 1 # shift one because list starts at 0


		if drawers[drawerToOpen][0] == True:
			print("Sorry, you can not open this drawer. It is locked.")
			sleep(2)
		elif drawers[drawerToOpen][1] == False:
			print("Sorry, you can not open this drawer. It is already open.")
			sleep(2)
		else:
			drawers[drawerToOpen][1] = False
			if drawers[drawerToOpen][4] == False:
				drawers[newDrawer][4] = True
		clear()
	elif action[:5] == "close":
		# number parsing
		drawerToClose = ""
		# length will be 7 if single digit, 8 if double digit
		if len(action) == 8:
			drawerToClose = int(action[-2:]) # slicing magic
		else:
			drawerToClose = int(action[-1:]) # slicing magic
		drawerToClose -= 1 # shift one because list starts at 0


		if drawers[drawerToClose][1] == True:
			print("Sorry, you can not close this drawer. It is already closed.")
			sleep(2)
		else:
			drawers[drawerToClose][1] = True
			drawers[drawerToClose][0] = True
			if drawers[drawerToClose][2] == None:
				drawers[drawerToClose][4] = False # unreserve when a surface is taken out

				#note: I am a massive idiot. i spent 2 hours trying to find why i wasn't setting the flag to false, when i said flag == false instead of flag = false

			# lock a drawer after it is closed, because locked is the default state
			# and it should only be open when a surface is being taken in or out 
		clear()
	elif action == "exit":
		break
	elif action == "add":
		newDrawer = None
		# find an open drawer
		for i in range(len(drawers)):
			if drawers[i][4] == False:
				newDrawer = i
				break
		if newDrawer == None:
			print("Sorry, all drawers are being used right now.")
		else:
			# get input
			newUsername = raw_input("Please enter your username.\n")
			newPassword = raw_input("Please enter your password.\n")
			# set information
			drawers[newDrawer][2] = newUsername
			drawers[newDrawer][3] = newPassword
			drawers[newDrawer][4] = True
			# unlock the drawer until it is opened and closed
			drawers[newDrawer][0] = False
			print("Please put your surface in drawer number " + str(newDrawer + 1) + ".")
		sleep(2)
		clear()
	elif action == "remove":
		drawerToUnlock = None
		username = raw_input("Please enter your username.\n")
		# find the drawer with a matching username
		for i in range(len(drawers)):
			if drawers[i][2] == username:
				drawerToUnlock = i
				break
		if drawerToUnlock == None:
			print("Sorry, no surface was found matching that username.")
			sleep(2)
		else:
			password = None
			while password != drawers[drawerToUnlock][3]:
				password = raw_input("Please enter your password.\n")
				if password != drawers[drawerToUnlock][3]:
					print("Incorrect password. Please try again.")
			drawers[drawerToUnlock][0] = False
			drawers[drawerToUnlock][2] = None
			drawers[drawerToUnlock][3] = None
			print("Please remove your surface from drawer number " + str(drawerToUnlock + 1) + ".")
			sleep(2)
		clear()
	elif action[:7] == "barcode":
		drawerToClose = None
		for i in range(len(drawers)):
			if drawers[i][1] == False:
				drawerToClose = i
				break
		if drawerToClose != None:
			print("Please close drawer number " + str(drawerToClose + 1) + ".")
		else:
			unlockedDrawer = None
			for i in range(len(drawers)):
				if drawers[i][0] == False:
					unlockedDrawer = i
					break
			if unlockedDrawer != None:
				if drawers[unlockedDrawer][4] == False:
					print("Please put your surface in drawer number " + str(unlockedDrawer + 1) + ".")
					drawers[unlockedDrawer][2] = action[-10:] # if a new barcode is scanned when an old drawer is still unlocked and doesn't have a surface in it, repurpose the drawer
				else:
					print("Please remove the surface from drawer number " + str(unlockedDrawer + 1) + ".")
			else:
				code = action[-10:] # because student ids are always 10 digits
				removeDrawer = None
				for i in range(len(drawers)): # check if you are removing or adding
					if drawers[i][2] == code:
						removeDrawer = i
				if removeDrawer == None: # add functionality
					newDrawer = None
					# find an open drawer
					for i in range(len(drawers)):
						if drawers[i][4] == False:
							newDrawer = i
							break
					if newDrawer == None:
						print("Sorry, all drawers are being used right now.")
					else:
						# set information
						drawers[newDrawer][2] = code
						# unlock the drawer until it is opened and closed
						drawers[newDrawer][0] = False
						print("Please put your surface in drawer number " + str(newDrawer + 1) + ".")
				else: # remove functionality
					drawers[removeDrawer][0] = False
					drawers[removeDrawer][2] = None
					drawers[removeDrawer][3] = None
					print("Please remove your surface from drawer number " + str(removeDrawer + 1) + ".")
		sleep(2)
		clear()	
	else:
		clear()


'''
Actions:
print list: prints out the current state of the list
open: opens a drawer
close: closes a drawer
exit: exits the program
add: requests to put a surface in a cabinet
remove: requests to remove a surface from a cabinet
barcode: simulate the scanning of a barcode
'''
