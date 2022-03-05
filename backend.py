# 1 - take get request from web server/pi, deliver database contents to web server/pi.
# 2 - take post request from web server/pi, update database accordingly.

# Stuff in DB - 
# sys 1-	# [1] Past Spendings that need to be payed by group (food, house shit, etc)
			# ID (integer), path to image (.png), Title, Date, Category, Description (optionally null), Cost, Payer (single ID), Compensated (bool), Date compensated
			# Manual creation of these things
			#
			# [2] Future Spendings (electricity, rent, water, internet)
			# ID, Title, Due date, Category, Description (optionally null), Cost, Payer (single ID), Paid (bool), Date paid
			# Manual creation of these things
			#
			# [3] Chores
			# ID, Title, Due date, Category, Description (optionally null), Chorer (single ID), Completed (bool), Date completed
			# Automated creation of the things (python script) - makes for the next month (run it every month)
			# Supports Manual creation
			# List of common ones (restock the fridge and shit)
			# 
			# [4] Commits to a new folder in git repo every day (cron job)
#
# sys 3 - [5] Homework
# Title, Due date, Category, Description, Completed, Date completed, homeworker (single ID)
#
# sys 3 - [6] Keep track of who's at the house
# if you're the last one out then lock up
# 
# sys 3 - [7] Discord bot
#
# sys 2 - [8] Username(s) / Password hash(es) in a JSON
#

#
# Generic Get - figures out the users and the time frame 
#
# Get - Users (array), Date before, Date after, which database
# DONE - Post - Add past spendings
# Post - Add chores
# Post - Add future spendings
# DONE - Post - Delete past spendings (ID)
# Post - Delete chores (ID)
# Post - Delete future spendings (ID)


# Flask? Requests?

# data = {
#     "president": {
#         "name": "Zaphod Beeblddddddbrox",
#         "species": "Betelgeusian"
#     }
# }

#print(data["president"]["name"])

# with open("./data/data_file.json", "w") as write_file:
#     json.dump(data, write_file)

# with open("./data/data_file.json", "r") as read_file:
#     data2 = json.load(read_file)

# print(data2["president"]["name"])

#############################

# This is an example of how to call data to/from a file

#############################

import json
from datetime import datetime
import time

# ID (integer), path to image (.png), Title, Date, Category, Description (optionally null), Cost, Payer (single ID), Compensated (bool), Date compensated

# Post - Add past spendings
# Post - Delete past spendings (ID)

# data = {
#     "president": {
#         "name": "Zaphod Beeblddddddbrox",
#         "species": "Betelgeusian"
#     }
# }



def saveD(database, data):
	with open("./data/" + database + ".json", "w") as write_file:
	    json.dump(data, write_file)

def openD(database):
	with open("./data/" + database + ".json", "r") as read_file:
	    data = json.load(read_file)
	    return data

##########################
# Load all the things in #
##########################

pastData = openD("past")
users = openD("users")

# time.strftime(r"%d.%m.%Y", time.localtime())

def addPast(Title, Category, Cost, Payer, Compensated = False, DateCompensated =None, Description=None, Date=datetime.now().strftime("%m.%d.%Y"), ImagePath=None):
	####################
	# Input Validation #
	####################

	userValid = False
	for i in users:
		if(Payer == i):
			userValid = True
			break
	if(userValid == False):
		print("Err - not valid user")
		return
	# if category exists, use it
	# if not, make a new one
	categoryNum = -1
	for i,j in enumerate(pastData["categories"]):
		if(Category == j):
			categoryNum = i
			#print(i) # USE THIS CATEGORY, position is here
	if(categoryNum < 0):
		### make a new category
		pastData["categories"].append(Category)
		saveD("past", pastData)
	
	##############
	# Add to DB  #
	##############
	newID = pastData["highestID"]
	newID = newID + 1
	#print(newID)

	pastData["highestID"] = newID

	pastData["data"][str(newID)] = {
		"Title": Title,
		"Category": Category,
		"Cost": Cost,
		"Payer": Payer,
		"Compensated": Compensated,
		"DateCompensated": DateCompensated,
		"Description": Description,
		"Date": Date,
		"ImagePath": ImagePath
	}
	saveD("past", pastData)
	return


addPast("x","k","0","Kaden")

#print(pastData["highestID"])
#print(users)



def delPast(ID):
	print(pastData["data"]["1"])
	del pastData["data"][str(ID)]
	saveD("past", pastData)
	return

#delPast(1)