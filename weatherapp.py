import requests
import json
import pyttsx3

def speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

city = input("enter name of the city: ")

url = f"https://api.weatherapi.com/v1/current.json?key=3ebf167bbac8448785893816240704&q={city}"


r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]

speech(f"the current weather in {city} is {w} degrees")


