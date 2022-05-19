
import os
import requests
from datetime import datetime, timedelta
import time
from colorama import Fore, Back, Style

############ VAR INPUTS ###########
api_key_weather = "1f64858882e3d5ea2b531cba94220279"
city_name = "Atlanta,us"
exclude = "minute,hourly"
url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&APPID={api_key_weather}&units=imperial'

# Get current date
now = datetime.now()

# How long from now we will be Hoochin
print("How many days from now are you shooting the Hooch?")
days_till = int(input())

# Get Datetime based on info
future_date = now + timedelta(days_till)
hooch_date = future_date.strftime('%Y-%m-%d')
forecasted_datetime = str(hooch_date) + " 12:00:00"

# Start + end time and concat with future date
print("What time (military) are you lookin to start Hooching?")
hooch_start_time = datetime.strptime(input(), '%H:%M')
start_datetime = datetime.combine(future_date.date(), hooch_start_time.time())
print("What time (military) are you planning on getting off the Hooch? (If ever)")
hooch_end_time = datetime.strptime(input(), '%H:%M')
end_datetime = datetime.combine(future_date.date(), hooch_end_time.time())

# Get Hoochers and Bevvie Count
print("How many people are annihilating the Chattahoochie? ")
num_hoochers = int(input())
print("Is Jake bringing a Date for Real?")
jake_date = input()
print("How many Bevvies do you have? ")
bevvies = int(input())
print("Bringing any Franzia with you? ")
franzi_yuh = input()

# CRITICAL!!! GET THE VIBE CHECK!!!!!
print("True or False - The Vibes are High this weekend ")
vibe_check = input()
if vibe_check != "True":
    print("Vibes can only be good.")
    print("With that in mind...True or False - The Vibes are High this weekend ")
    vibe_check = input()

print("The forcasted datetime is " + forecasted_datetime)

####### GET LIVE WEATHER FORECAST #######
req = requests.get(url)
data = req.json()
for i in data['list']:
    if i['dt_txt'] == forecasted_datetime:
        description = i["weather"][0]["description"]
        forecasted_temp = i['main']['temp']

####### TESTS ON WATER QUALITY #######
def water_quality(hooch_date):
    water_tests = [
        "e.coli quality on " + hooch_date,
        "Average water Temperature on " + hooch_date
    ]
    for l in water_tests:
        print(l, Back.GREEN + "PASS!" + Style.RESET_ALL)
        time.sleep(2)

####### TESTS ON WEATHER #######
def weather_quality(forecasted_temp):
    print("Testing the weather...")
    if float(forecasted_temp) < 80.00:
        print(Back.RED + "The temperature of " + str(forecasted_temp) + " is too low.  Keep an eye out for this one!" + Style.RESET_ALL)
    else:
        print(Back.GREEN + "The temperature of " + str(forecasted_temp) + " is fucking epic dude.  Lets ride!")

####### TESTS ON THE VIBE OF THE MANGO #######
def overall_vibe(num_hoochers, jake_date, vibe_check, bevvies, franzi_yuh):
    if jake_date != "no":
        num_hoochers = num_hoochers + 1
        print("Oh snap no way Jake is bringing a date on the high seas!")
    if franzi_yuh != "no":
        bevvies = bevvies + 10
        print("Hell yeah dude we are about to slap that bag!")
    drinks_person = bevvies / num_hoochers
    if drinks_person < 6:
        print(Back.RED + "Sorry folks, " + str(drinks_person) + " drinks per person is simply not enough beverages per person. Head back over to Publix and grab a case of the Rockies!" + Style.RESET_ALL)
    else:
        if franzi_yuh != "no":
            print(Back.GREEN + "Heck Yeah you have " + str(drinks_person) + "drinks per person and you have a bag-o-blush! Get up in a tree and start slapping that bad boy!" + Style.RESET_ALL)
        else:
            print(Back.GREEN + "You did it! With" + str(drinks_person) + " drinks per person, you have enough drinks for the Hooch!" + Style.RESET_ALL)

weather_quality(forecasted_temp)
water_quality(hooch_date)
overall_vibe(num_hoochers, jake_date, vibe_check, bevvies, franzi_yuh)