import speech_recognition as sr
import pyttsx3
import openai
from playsound import playsound
import time
import os

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
        # openai.organization = "openai_organization"
        # openai.api_key = "openai_api_key"
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voices', self.voices[1].id)
        
        self.r, self.mic = ft_microphone()
        
        self.conversation = ""
        self.user_name = "Dan"
        self.bot_name = "John"

    def ft_user_input(self):
        # if self.mic != "":
        #     self.r, self.mic = ft_microphone()
        with self.mic as source:
            playsound('sons/beep_audio.mp3')
            print("\n Listening...")
            self.r.adjust_for_ambient_noise(source, duration=0.2)
            audio = self.r.listen(source, timeout=5, phrase_time_limit=10)
        print("no longer listening")
        try:
            user_input = self.r.recognize_google(audio)
        except:
            user_input = "Error"
        # print(user_input)

        return user_input

    def ft_response_write(self, user_input):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=user_input,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        response_str = response["choices"][0]["text"].replace("\n", "")
        # response_str = "I'm fine thank you, and you ? how are you today ?"
        response_str =response_str.split(
            user_name + ":" ,1)[0].split(bot_name+ ":",1)[0]
        # print(response_str)

        return response_str

    def ft_response_vocal(self, response):
        self.engine.say(response)
        self.engine.runAndWait()

