import datetime
import request
import json

# Here is a program to show how to use "if - elif - else"
# The hash-tag is used to show that these are comments
# This means that the computer will not look at these lines
# Author: Mr. Jugoon
# Upper Canada College

# Put down some options for the user to choose from...
api_key = "05b6b9b076a3ba64b4d4c3ca9d12a2aa"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

print("1. Weather \n 2. Time \n 3. Who was the last monarch of Albania?\n")

choice = input("What is your current mood? (Please type a number!): ")


try:
	choice = round(int(choice), 0) #What I want to run when the person runs a number
except ValueError: #Number in place of string and vice versa
	print("Please re-run the program. And input a number!!!!") #When someone types a string

if choice == 1:

	#Input
	city = input("What city would you like to know the weather of: ") #Check the city name
	
	#Getting Weather
	complete_url = base_url + "appid=" + api_key + "&q=" + city_name #What the API accepts
	response = requests.get(complete_url) 

	results = response.json()
	main = results["main"]

	current_temp = main["temp"] - 273.15 #Convert Kelvin to Celsius
	current_weather = results["weather"][0]["description"]

	#Output
	print(f"The weather is described as '{str(current_weather)}' and it is {str(current_temp)} degrees celsius")
elif choice == 2:
	now = datetime.datetime.now()

	print(now.strftime("%Y-%m-%d %I:%M"))
elif choice == 3:
	print("Kind Zog! Duh")

if mood == 1:
    print("That's awesome!")
elif mood == 2:
    print ("Can I cheer you up?")
elif mood == 3:
    print ("I am very happy for you!")
else:
    print ("This is not a valid choice")
    print ("Hope you have a great day anyway!")


# This is a way to gracefuuly exit the program
input("Press ENTER to quit the program")
