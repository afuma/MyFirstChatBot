# code fonctionne

import speech_recognition as sr
# import pyttsx3
# import openai
import time

def ft_microphone():
    micros = sr.Microphone.list_microphone_names()
    for index, micro in enumerate(micros):
        if (micro == "default"):
            index_micro = index
            break

    r = sr.Recognizer()
    mic = sr.Microphone(device_index=index_micro)

    return (r, mic)
    
class ChatEnglish():

    def __init__(self):
        # self.engine = pyttsx3.init()
        # self.voices = self.engine.getProperty('voices')
        # self.engine.setProperty('voices', self.voices[1].id)
        # self.r, self.mic = ft_microphone()
        pass

    def ft_user_input(self):
        r, mic = ft_microphone()
        with mic as source:
            print("\n Listening...")
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
        print("no longer listening")

        try:
            user_input = r.recognize_google(audio)
        except:
            user_input = "Error"

        print(user_input)
        return user_input


if __name__ == '__main__':
    chat = ChatEnglish()
    print(chat.ft_user_input())