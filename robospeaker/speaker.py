# import os
#
# if __name__ == '__main__':
#     print("Welcome to robospeaker")
#     x = input("enter what you want me to speak: ")
#     command = f"say {x}"
#     os.system(command)

import pyttsx3
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    print("Welcome to robospeaker")

    while True:
        x = input("Enter what you want me to speak (to exit, type 'q'): ")
        if x.lower() == "q":
            text_to_speech("bye bye friend.")
            break
        text_to_speech(x)
