## Run this command in terminal  before executing this program
## rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml
## and also run this in seperate terminal
## rasa run actions

import requests
#import speech_recognition as sr     # import the library
#import subprocess
#from gtts import gTTS

sender = input("What is your name?\n")

bot_message = ""
while bot_message != "Bye":
    message = input("What's your message?\n")

    print("Sending messages now...")

    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"sender": sender, "message": message})

    print("Bot says, ",end=' ')
    for i in r.json():
        bot_message = i['text']
        print(f"{bot_message}")

#    subprocess.call(['mpg321', "welcome.mp3", '--play-and-exit'])