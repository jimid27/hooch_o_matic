
import os
import requests
from datetime import datetime, timedelta
import time
from colorama import Fore, Back, Style

############ VAR INPUTS ###########
count_pass = 0
count_fail = 0
api_key_weather = os.getenv('API_KEY_WEATHER') # Get API Key for openweathermap from os env
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
# See if that rascal is bringing a date on the Hooch
print("Is Jake bringing a Date for Real?")
jake_date = input()
if jake_date != "no":
    num_hoochers = num_hoochers + 1
    print(Back.GREEN + "Oh snap no way Jake is bringing a date on the high seas!" + Style.RESET_ALL)
# Get a can count
print("How many canned Bevvies do you have? ")
bevvies = int(input())
# Get a quick franzia check
print("Bringing any Franzia with you? ")
franzi_yuh = input()
if franzi_yuh != "no":
    bevvies = bevvies + 10
    print(Back.MAGENTA + "Hell yeah dude we are about to slap that bag!" + Style.RESET_ALL)

# CRITICAL!!! GET THE VIBE CHECK!!!!!
print("True or False - The Vibes are High this weekend ")
vibe_check = input()
if vibe_check != "True":
    print("Vibes can only be good.")
    print("With that in mind...True or False - The Vibes are High this weekend ")
    vibe_check = input()

####### GET LIVE WEATHER FORECAST #######
req = requests.get(url)
data = req.json()
for i in data['list']:
    if i['dt_txt'] == forecasted_datetime:
        description = i["weather"][0]["description"]
        forecasted_temp = i['main']['temp']
        precip_chance = float(i['pop'])*100

def prerequisites():
    global count_pass
    global count_fail
    print("Checking prerequisite items for Hooching...")
    prerequisite_items = [
        "Do we have at least 1 paddle? ",
        "Do we have at least 1 JBL Xtreme 2 speaker for tunes? ",
        "Do we have the Baptized in the Chattahoochie Playlist downloaded? ",
        "Do we have the H.O.O.C.H system in place? ",
        "Has everyone played TWDIHDIHOTINPLFT? ",
        "Do we have an updated tube chart ready to go? ",
        "Do we have all tubes accounted for in our Chart? "
    ]
    for l in prerequisite_items:
        print(l, Back.GREEN + "PASS!" + Style.RESET_ALL)
        count_pass += 1
        time.sleep(2)
####### TESTS ON WATER QUALITY #######
def water_quality(hooch_date):
    global count_pass
    global count_fail
    water_tests = [
        "e.coli quantity on " + hooch_date,
        "Average water Temperature on " + hooch_date,
        "Average water velocity on " + hooch_date,
        "Average water height on " + hooch_date,
        "Ability for at least one person to save someone's life if the fall over on " + hooch_date,
        "Rob or Jimi onboard to swim group to island on " + hooch_date
    ]
    for l in water_tests:
        print(l, Back.GREEN + "PASS!" + Style.RESET_ALL)
        count_pass += 1
        time.sleep(2)

####### TESTS ON WEATHER #######
def weather_quality(forecasted_temp, description):
    global count_pass
    global count_fail
    print("Testing the weather...")
    time.sleep(2)
    if float(forecasted_temp) < 75.00:
        print("The temperature of " + str(forecasted_temp) + " is a bit too low.  Keep an eye out for this one! " + Back.RED + "FAIL" + Style.RESET_ALL)
        count_fail += 1
    elif description.__contains__('rain'):
        if precip_chance > 40.00:
            print("Oh no! The chance of rain at that time is " + str(precip_chance) + " which is higher than the allowed threshhold. Might want to hold off on this one. " + Back.RED + "FAIL" + Style.RESET_ALL)
            count_fail += 1
        else:
            print("Looks like the chance of rain during Hooch time exists but is pretty low at " + str(precip_chance) + "%. Lets Party! " + Back.GREEN + "PASS" + Style.RESET_ALL)
            count_pass += 1
    else:
        print("The temperature of " + str(forecasted_temp) + " is freaking epic dude and doesn't look like it's gonna rain.  Lets ride! " + Back.GREEN + "PASS" + Style.RESET_ALL)
        count_pass += 1

####### TESTS ON THE VIBE OF THE MANGO #######
def overall_vibe(num_hoochers, jake_date, vibe_check, bevvies, franzi_yuh):
    global count_pass
    global count_fail
    vibe_check_tests = [
        "Is everyone ready to absolutely Vibe?",
        "Do we have volunteers to work and put the two halves of the tube "
        ""
    ]
    drinks_person = bevvies / num_hoochers
    if drinks_person < 6:
        print("Sorry folks, " + str(drinks_person) + " drinks per person is simply not enough beverages per person. Head back over to Publix and grab a case of the Rockies! " + Back.RED + "FAIL" + Style.RESET_ALL)
        count_fail += 1
    else:
        if franzi_yuh != "no":
            print("Heck Yeah you have " + str(drinks_person) + " drinks per person and you have a bag-o-blush! Get up in a tree and start slapping that bad boy! " + Back.GREEN + "PASS" + Style.RESET_ALL)
            count_pass += 1
        else:
            print("You did it! With" + str(drinks_person) + " drinks per person, you have enough drinks for the Hooch! " + Back.GREEN + "PASS" + Style.RESET_ALL)
            count_pass += 1

prerequisites()
weather_quality(forecasted_temp, description)
water_quality(hooch_date)
overall_vibe(num_hoochers, jake_date, vibe_check, bevvies, franzi_yuh)
print(str(count_pass))