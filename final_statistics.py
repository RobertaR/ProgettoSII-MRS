#### PROGETTO SII - MOVIE RECOMMENDER SYSTEM

#### ROBERTA ROMANO

from ClassUsers_Items import *

import re

users = []

# Load the movie lens dataset into arrays
d = Dataset()
d.load_final_user_ratings("data/us.user", users)
def print_user(user):
	return user.name + "|" + str(user.age) + "|" + user.sex + "|" + user.occupation + "|" + user.education + "|" + str(user.rating)

def getSex(sex):
	text = ""
	for u in users:
		if u.sex == sex:
			text = text + "\n" + print_user(u)
	return text

def getOccupation(occupation):
	text = ""
	for u in users:
		if u.occupation == occupation:
			text = text + "\n" + print_user(u)
	return text

def getAge(age):
	text = ""
	split_age = age.split("-")

	for u in users:
		if int(u.age) >= int(split_age[0]) and int(u.age) <= int(split_age[1]):
			text = text + "\n" + print_user(u)
	return text

def getEducation(education):
	text = ""
	for u in users:
		if u.education == education:
			text = text + "\n" + print_user(u)
	return text

def getRating(number):
	text = ""
	for u in users:
		if int(u.rating) == number:
			text = text + "\n" + print_user(u)

	return text


if __name__ == '__main__':

	#print users

	sex = ["F","M"]
	occupation = ["student", "administrator","artist","doctor","educator","engineer","entertainment","executive","healthcare", "housewife","homemaker","lawyer","librarian","marketing","none","programmer","retired","salesman","scientist","technician","writer","other"]
	education = ["None", "Secondary", "Degree", "PhD"]
	age_ranges = ["10-20", "21-30", "31-40", "41-50", "51-60", "61-70"]

	#getHigherRatings()
	string_div_categories = "----------------------------------------"
	string_div_same_category = "****************************************"

	statisticsFile = open('data/statistics.txt', 'a')

	for s in sex:
		statisticsFile.write("\n" + string_div_categories + "\n" + "Sorted by Sex: "+ s + "\n" + getSex(s) + "\n" + string_div_same_category)

	for o in occupation:
		statisticsFile.write("\n" + string_div_categories + "\n" + "Sorted by Occupation: "+ o + "\n" + getOccupation(o)+ "\n" + string_div_same_category)
	
	for e in education:
		statisticsFile.write("\n" + string_div_categories + "\n" +  "Sorted by Occupation: "+ e + "\n" + getEducation(e)+ "\n" + string_div_same_category)

	for a in age_ranges:
		statisticsFile.write("\n" + string_div_categories + "\n" + "Sorted by Age Ranges: "+ a + "\n" + getAge(a)+ "\n" + string_div_same_category)

	for n in range(1,6):
		statisticsFile.write("\n" + string_div_categories + "\n" + "Sorted by Rating: "+ str(n) + "\n" + getRating(n)+ "\n" + string_div_same_category)

	statisticsFile.close()
	