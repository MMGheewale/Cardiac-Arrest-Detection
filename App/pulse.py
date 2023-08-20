from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.graph import MeshLinePlot
from kivy.clock import Clock
from threading import Thread
import urllib.request
import requests
import threading
import json
import re
import random
from kivy.config import Config 
Config.set('graphics', 'resizable', True) 
import kivy 
kivy.require('1.9.0') 
from kivy.uix.label import Label 
from kivy.uix.spinner import Spinner 
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from functools import partial
import threading
from kivy.core.audio import SoundLoader
from kivy.properties import BooleanProperty, StringProperty
global e
e=0
global e_exit
e_exit=0
import time

def get_pulse_level():
    global levels
    global e_exit
    e_exit=0
    levels=[]
    global e
    i=0
    start_time = time.time()
    global pulse
    pulse=0
    
    def low_beep():
        sound = SoundLoader.load('low.mp3')
        if sound:
            sound.play()
    def normal_beep():
        sound1 = SoundLoader.load('normal.mp3')
        if sound1:
            sound1.play()
    def high_beep():
        sound2 = SoundLoader.load('high.mp3')
        if sound2:
            sound2.play()
    while True:
        if((time.time() - start_time) >= 60):
            levels=[]
            print("1 minutes done levels contain: ",levels,"\n")
            start_time= time.time();
            
        URL='https://api.thingspeak.com/channels/1370563/fields/1.json?api_key=HX7TNEUYXRKQEVRO'
        HEADER='&results=1'
        NEW_URL=URL+HEADER
        get_data=requests.get(NEW_URL).json()
        feild_1=get_data['feeds']
        for x in feild_1:
            pulse=int(x['field1'])
            levels.append(int(int(x['field1'])))
            print(int(int(x['field1'])))
        if((int(int(x['field1']))<60) and (e==1)):
            low_beep()
            print("check")
        elif((int(int(x['field1']))<120) and (e==1)):
            normal_beep()
            print("check1")
        elif(e==1):
            high_beep()
            print("check2")
        if(e_exit==1):
            print("thead exit")
            levels=[]
            break

class Logic(BoxLayout):
    pulse_label_value = StringProperty()
    global pulse
    def __init__(self, **kwargs):
        super(Logic, self).__init__(**kwargs)
        self.plot = MeshLinePlot(color=[1, 0, 0, 1])
        Clock.schedule_interval(lambda dt: self.update_time(), 1)
        
    def update_time(self):
        self.pulse_label_value = "Heart Beat: "+str(pulse)
            

    def start(self):
        global e
        e=1
        global e_exit
        e_exit=0
        self.ids.graph.add_plot(self.plot)
        Clock.schedule_interval(self.get_value,1)

    def stop(self):
        global e
        e=0
        Clock.unschedule(self.get_value)

    def get_value(self, dt):
        self.plot.points = [(i, j) for i, j in enumerate(levels)]

    def home(self):
        global e
        e=0
        global e_exit
        e_exit=1
        Clock.unschedule(self.get_value)
        self.clear_widgets()
        App().get_running_app().stop()
        import home
        home.home()


class RealTimePulse(App):
    def build(self):
        return Builder.load_file("look.kv")

def run():
    levels = []  # store levels of microphone
    get_level_thread = Thread(target = get_pulse_level)
    get_level_thread.daemon = True
    get_level_thread.start()
    RealTimePulse().run()
    
