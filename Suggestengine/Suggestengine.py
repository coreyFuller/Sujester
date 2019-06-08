import requests
import bs4
import RandomHeaders
import sys
import easygui as eg
import random
import datetime

now = datetime.datetime.now()

URL = "https://calendar.clemson.edu/"
SECTION_CSS = ".vevent"
TIME = ".dtstart"
LOCATION = ".event_item_venue"
EVENT = ".summary a"

def grab_site(url):
	# Pulls the site
	headers = RandomHeaders.LoadHeader()
	# This is a non-Python user agent, which prevents Amazon from blocking the request
	return requests.get(url, headers=headers)

event_list = []
place_list = []
when_list = []
if __name__ == '__main__':
	res = grab_site(URL)
	page = bs4.BeautifulSoup(res.text, 'lxml')

	try:
		for section in page.select(SECTION_CSS):
			event = section.select(EVENT)
			time = section.select(TIME)
			location = section.select(LOCATION)

			event = event[0].getText()
			time = time[0].getText()
			location = location[0].getText()

			time = time.translate({ord(c): None for c in '\n'})

			time = time[4:]

			event_list.append(event)
			place_list.append(location)
			when_list.append(time)

	except:
		pass

sys.path.append('..')

reply = eg.buttonbox("\t\tWelcome to the Sujestr, brought to you by Nudl", choices = ['I want ideas!'])
if reply is None:
	exit()
else:
	choices = ["Clemson Event", "Spontaneous"]
	reply = eg.buttonbox("Make a pick:", choices  = ['One Time Events', 'Anytime Events'])

	if reply is None or reply == 'One Time Events':
		choices = ["This Month", "This Week", "Right Now", "Done"]
		reply = eg.buttonbox("When would you like to attend this event?", choices = ['This Month','This Week', 'Right Now', 'Done'])
		if reply is None or reply == 'Done':
			exit()
		elif reply == 'This Month':
			while reply is not "Done":
				x = random.randint(0, len(event_list)-1)
				reply = eg.buttonbox(("Sure thing. Here's something I've found: "+str(event_list[x]) +" at "+str(place_list[x]) + " " +str(when_list[x])), choices = ["Another Idea?", "Done"])

		elif reply == 'This Week':
			today = now.day
			month = now.month
			date = str(month) + "/" + str(today)

			todayEvents = []
			tEvTime = []
			tEvLoc = []

			for y in range(0,6):
				for x in range(len(event_list)):
					if str(month) + "/" + str(today+y) in when_list[x]:
						todayEvents.append(event_list[x])
						tEvLoc.append(place_list[x])
						tEvTime.append(when_list[x])

			if len(todayEvents) != 0:
				while reply is not "Done":
					x = random.randint(0, len(todayEvents)-1)
					date = todayEvents[x]
					reply = eg.buttonbox(("OK, I've got something you might be interested in, " +str(date) + " at " + str(tEvLoc[x]) + ", " + str(tEvTime[x])), choices = ["Another Idea?", "Done"])

		elif reply == 'Right Now':
			today = now.day
			month = now.month
			date = str(month) + "/" + str(today)

			todayEvents = []
			tEvTime = []
			tEvLoc = []
			for x in range(len(event_list)):
				if date in when_list[x]:
					todayEvents.append(event_list[x])
					tEvLoc.append(place_list[x])
					tEvTime.append(when_list[x])

			if len(todayEvents) != 0:
				while reply is not "Done":
					x = random.randint(0, len(todayEvents)-1)
					date = todayEvents[x]
					reply = eg.buttonbox(("Alright. Here's what I've found for you:"+ str(date) + " at " + str(tEvLoc[x]) + ", " + str(tEvTime[x])), choices = ["Another Idea?", "Done"])
			else:
				eg.msgbox("Sorry, I found no events for today, perhaps you want to try later on")



	elif reply is None or reply == 'Anytime Events':
		choices = [ "Food", "Outdoors", "Sports", "etc.", "Done"]
		reply = eg.buttonbox("Choose an activity.", choices = ['Clubs','Food', 'Outdoors', 'Sports', 'Shopping', 'Etc.', 'Done'])
		xReply = reply
		while reply is not "Done":
				reply = xReply
				if reply is None or reply == 'Done':
					exit()
				elif reply =='Food':
					edible = ["try a bite at douthit dining hall", "take a trip to core dining hall", "try downtown's many fine dining locations",
"take a trip to Greenville", "TDs", "take a car ride to Anderson"]
					x = random.randint(0, len(edible)-1)
					reply = eg.buttonbox("If you want to do something of an consumable nature, you could "+str(edible[x]), choices = ['Another idea?', 'Done'])

				elif reply == 'Outdoors':
					outdoorsy = ["going to a park", "walking the dog", " taking a hike to the botanical gardens for the museum and garden", "visiting Lake Hartwell",
					"visiting the twin lakes" , "visiting y beach" ,"going to the dam", "experimenting with new forest hiking trails"]
					x = random.randint(0, len(outdoorsy)-1)
					reply = eg.buttonbox("If you want to do something outdoorsy, you could try " +str(outdoorsy[x]), choices = ['Another idea?', 'Done'])


				elif reply == 'Sports':
					sporty = ["going to bownam with friends", "going to union game center"]
					x = random.randint(0, len(sporty)-1)
					reply = eg.buttonbox("If you want to do something sporty, you could try " +str(sporty[x]), choices = ['Another idea?', 'Done'])


				elif reply == 'Shopping':
					money = ["going to the Walmart", "going to the Anderson mall", "going downtown Clemson", "checking out Alumni Hall", "looking at Tiger Sports",
					"staying at home and browsing Amazon"]
					x = random.randint(0, len(money)-1)
					reply = eg.buttonbox("If you have money burning a hole in your pocket, you could spend it by " +str(money[x]), choices = ['Another idea?', 'Done'])



				elif reply == 'Clubs':
					money = ["going to the chess club", " going to the boxing club", " going to the Dance club", "try out bass fishing",
					"look in on the Rubick's Cube club", "go to the Smash Bros. club"]
					x = random.randint(0, len(money)-1)
					reply = eg.buttonbox("Want to spend time with some like-minded people? Try " +str(money[x]), choices = ['Another idea?', 'Done'])


				elif reply == 'Etc.':
					chaos = ["going to the chess club", " going to the boxing club", "going to the Walmart", "going to the Anderson mall", "going downtown Clemson",
					"going to bownam with friends", "going to union game center", "going to a park", "walking the dog", " taking a hike to the botanical gardens for the museum and garden", "visiting Lake Hartwell"
				 	"visiting the twin lakes" , "visiting y beach" ,"going to the dam", "experimenting with new forest hiking trails", "a bite at douthit dining hall", "taking a trip to core dining hall", "downtown's many fine dining locations",
				 	"taking a trip to Greenville", "TDs", "take a car ride to Anderson"]
					x = random.randint(0, len(chaos)-1)
					reply = eg.buttonbox("Try " +str(chaos[x]), choices = ['Another idea?', 'Done'])
