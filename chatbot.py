from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivy.properties import StringProperty, ListProperty, NumericProperty
from kivy.core.text import LabelBase
from kivy.uix.anchorlayout import AnchorLayout

import multiexpressionbutton as meb
from Assistant import *
import time
# from threading import Thread
import threading

Window.size = (550, 750)

# ---------------------------------------------------------------------

class Command(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "Poppins"
    font_size = 17

# ---------------------------------------------------------------------

class Response(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "Poppins"
    font_size = 17

# ---------------------------------------------------------------------

class CircularProgressBar(AnchorLayout):
    set_value = NumericProperty(0)
    value = NumericProperty(0)
    bar_color = ListProperty([1, 0, 100/255])
    bar_width = NumericProperty(3)
    text = StringProperty("0%")
    # duration = NumericProperty(1.5)
    counter = 0

    def __init__(self, **kwargs):
        super(CircularProgressBar, self).__init__(**kwargs)
        # Clock.schedule_once(self.animate, 0)

    def animate(self, *args):
        Clock.schedule_interval(self.percent_counter, 0.35)

    def percent_counter(self, *args):
        if self.counter < self.value:
            self.counter += 1
            self.text = f"{self.counter}%"
            self.set_value = self.counter
        else:
            Clock.unschedule(self.percent_counter)

# ---------------------------------------------------------------------
 
class CustomThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        threading.Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
 
    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)
             
    def join(self, *args):
        threading.Thread.join(self, *args)
        return self._return

# ---------------------------------------------------------------------

class MultipleThread():

        def __init__(self, func1=None, args1=(), func2=None, args2=(), is_return_value=0):
            if (is_return_value):
                t = CustomThread(target=func1)
            else:
                t = threading.Thread(target=func1)
            t.start()

# ---------------------------------------------------------------------

class ChatBot(MDApp):

    def change_screen(self, name):
        screen_manager.current = name

    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        self.ICON = {
          'human_talk': 'images/human_talk.png',
          'ai_talk': 'images/ai_talk.png'
        }
        # self.circularProgressBar = CircularProgressBar()
        # screen_manager.add_widget(Builder.load_file("Main.kv"))
        screen_manager.add_widget(Builder.load_file("Chats2.kv"))
        self.assistant = ChatEnglish()
        self.response = ""
        self.conversation = ""
        self.nb_error = 0
        # self.st = CustomThread(target=self.assistant.ft_user_input)
        # self.first_thread = threading.Thread(target=screen_manager.get_screen('chats').circle_bar_voice.animate)

        return screen_manager

    def bot_name(self):
        if screen_manager.get_screen('main').bot_name.text != "":
            screen_manager.get_screen('chats').bot_name.text = screen_manager.get_screen('main').bot_name.text
            screen_manager.current = "chats"

    def ft_response(self, *args):
        self.response = "ya, i'm feel so good man" # self.assistant.ft_response_write(value)
        self.conversation += self.response
        screen_manager.get_screen('chats').chat_list.add_widget(Response(text=self.response, size_hint_x=.75))

    def send(self):
        global size, halign, value
        if screen_manager.get_screen('chats').text_input != "":
            value = screen_manager.get_screen('chats').text_input.text
            if len(value) < 6:
                size = .22
                halign = "center"
            elif len(value) < 11:
                size = .32
                halign = "center"
            elif len(value) < 16:
                size = .45
                halign = "center"
            elif len(value) < 21:
                size = .58
                halign = "center"
            elif len(value) < 26:
                size = .71
                halign = "center"
            else:
                size = .77
                halign = "left"
        screen_manager.get_screen('chats').chat_list.add_widget(Command(text=value, size_hint_x=size, halign=halign))
        Clock.schedule_once(self.ft_response, 2)
        screen_manager.get_screen('chats').text_input.text = ""

    def ft_humantalk(self):
        print('long press')
        # screen_manager.get_screen('chats').circle_bar_voice.animate()
        # user_input = self.assistant.ft_user_input()
        MultipleThread(func1=self.assistant.ft_user_input, is_return_value=1)
        MultipleThread(func1=screen_manager.get_screen('chats').circle_bar_voice.animate, is_return_value=0)
        # user_input = self.st.join()
        # print("user_input: " + str(user_input))
        user_input = "Error"
        if user_input == "Error":
            self.nb_error += 1
            screen_manager.get_screen('chats').infos_app.text = "Error " + str(self.nb_error)
        else:
            screen_manager.get_screen('chats').infos_app.text = ""
            screen_manager.get_screen('chats').text_input.text = user_input
            self.conversation += "\n" + user_input

    def ft_aitalk(self):
        try:
            # print("coucou les gars")
            if self.response != "":
                self.assistant.ft_response_vocal(self.response)
        except NameError:
            pass

if __name__ == '__main__':
    LabelBase.register(name="Poppins", fn_regular="polices/Poppins-Regular.ttf")
    ChatBot().run()