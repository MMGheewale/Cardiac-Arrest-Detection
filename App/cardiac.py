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
global e1
e1=0
global e_exit1
e_exit1=0
import time
from kivy.properties import BooleanProperty, StringProperty


def get_cardiac_level():
    global levels1
    global e_exit1
    e_exit1=0
    levels1=[]
    global e1
    e1=0
    warning_level=0
    value=0
    start_time1 = time.time()
    global assign_level
    assign_level=0
    
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
        if((time.time() - start_time1) >= 60):
            levels1=[]
            print("1 minutes done levels contain: ",levels1,"\n")
            start_time1= time.time();
            
        URL1='https://api.thingspeak.com/channels/1370563/feeds.json?api_key=HX7TNEUYXRKQEVRO&results=1'
        get_data1=requests.get(URL1).json()
        data1 = get_data1['feeds']
        
        for x1 in data1:        
            bpm = int(x1['field1'])
            rr =  int(x1['field2'])
            st =  int(x1['field3'])
            print("bpm: ",bpm,"rr: ",rr,"st: ",st)
            
        if(bpm<=50 or bpm>=150):
            warning_level=1
            if(rr<=650 or rr>=950):
                warning_level=2
                if(st<=300 or st>=500):
                    warning_level=3
        else:
            warning_level=0

        
                    
        val= 2  if warning_level==0 else 25 if  warning_level==1 else 50 if warning_level==2 else 75 if warning_level==3 else 100
        val= int(val)
        print("warning_level: ",warning_level,"graph value: ", val)
        
        levels1.append(val)
        
        assign_level=val

        if(warning_level==1 and e1==1):
            normal_beep()
        elif(warning_level==2 and e1==1):
            high_beep()
        elif(warning_level==3 and e1==1):
            low_beep()
        if(e_exit1==1):
            levels1=[]
            print("thead exit")
            break

class Logic1(BoxLayout):
    cardiac_label_value = StringProperty()
    
    def __init__(self, **kwargs):
        super(Logic1, self).__init__(**kwargs)
        self.plot1 = MeshLinePlot(color=[1, 0, 0, 1])
        Clock.schedule_interval(lambda dt: self.update_time1(), 1)
        
    def update_time1(self):
        level_msg="normal"
        global assign_level
        
        if(assign_level==2):
            level_msg="normal"
        else:
            level_msg= str(assign_level)+" % Chances"
        self.cardiac_label_value = level_msg
            

    def start1(self):
        global e1
        e1=1
        global e_exit
        e_exit1=0
        self.ids.graph.add_plot(self.plot1)
        Clock.schedule_interval(self.get_value1,1)

    def stop1(self):
        global e1
        e1=0
        Clock.unschedule(self.get_value1)

    def get_value1(self, dt1):
        self.plot1.points = [(i, j) for i, j in enumerate(levels1)]

    def home1(self):
        global e1
        e1=0
        global e_exit1
        e_exit1=1
        Clock.unschedule(self.get_value1)
        self.clear_widgets()
        App().get_running_app().stop()
        import home
        home.home()


class RealTimeCardiac(App):
    def build(self):
        return Builder.load_file("cardiac.kv")

def run():
    levels = []  # store levels of microphone
    get_level_thread1 = Thread(target = get_cardiac_level)
    get_level_thread1.daemon = True
    get_level_thread1.start()
    RealTimeCardiac().run()
    
