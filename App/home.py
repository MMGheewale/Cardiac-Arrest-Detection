from kivy.config import Config 
Config.set('graphics', 'resizable', True) 
import kivy 
from kivy.app import App 
kivy.require('1.9.0') 
from kivy.uix.label import Label 
from kivy.uix.spinner import Spinner 
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from functools import partial
import main
import userinfo

class SpinnerExample(App):
    def callback(self, layout):
        layout.clear_widgets()
        App().get_running_app().stop()
        main.abc()
        
    def build(self):
        layout = FloatLayout()
        self.btn = Button(text ="User Information", 
        color =(1, 0, .65, 1), 
        size_hint = (.4, .1),
        pos_hint = {"x":0.30, "y":0.80}) 
        def e():
                layout.clear_widgets()
                App().get_running_app().stop()
                userinfo.home()
        self.btn.bind(on_press=lambda x: e())
        layout.add_widget(self.btn)


        self.btn1 = Button(text ="ECG Signal", 
        color =(1, 0, .65, 1), 
        size_hint = (.4, .1),
        pos_hint = {"x":0.30, "y":0.60}) 
        def e1():
                import pulse
                layout.clear_widgets()
                App().get_running_app().stop()
                pulse.run()
        self.btn1.bind(on_press=lambda x1: e1())
        layout.add_widget(self.btn1)


        self.btn2 = Button(text ="Cardiac Arrest Detection", 
        color =(1, 0, .65, 1), 
        size_hint = (.4, .1),
        pos_hint = {"x":0.30, "y":0.40}) 
        def e2():
                import cardiac
                layout.clear_widgets()
                App().get_running_app().stop()
                cardiac.run()
        self.btn2.bind(on_press=lambda x: e2())
        layout.add_widget(self.btn2)        


        self.logout = Button(text ="LOGOUT", 
        color =(1, 0, .65, 1), 
        size_hint = (.2, .1),
        pos_hint = {"x":0.40, "y":0.10}) 

        self.logout.bind(on_press=lambda x: self.callback(layout))
        layout.add_widget(self.logout)
        return layout; 

def home():
    SpinnerExample().run()	 
