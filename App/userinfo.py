from kivy.config import Config 
import pymysql
Config.set('graphics', 'resizable', True) 
import kivy 
from kivy.app import App 
kivy.require('1.9.0') 
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner 
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.properties import BooleanProperty, ObjectProperty
from functools import partial
import main


class SpinnerExample(App):
    def callback(self, layout):
        layout.clear_widgets()
        App().get_running_app().stop()
        main.abc()
        
    def build(self):
        class EditableLabel(Label):
            edit = BooleanProperty(False)

            textinput = ObjectProperty(None, allownone=True)

            def on_touch_down(self, touch):
                if self.collide_point(*touch.pos) and not self.edit:
                    self.edit = True
                return super(EditableLabel, self).on_touch_down(touch)

            def on_edit(self, instance, value):
                if not value:
                    if self.textinput:
                        self.remove_widget(self.textinput)
                    return
                self.textinput = t = TextInput(
                        text=self.text, size_hint=(None, None),
                        font_size=self.font_size, font_name=self.font_name,
                        pos=self.pos, size=self.size, multiline=False)
                self.bind(pos=t.setter('pos'), size=t.setter('size'))
                self.add_widget(self.textinput)
                t.bind(on_text_validate=self.on_text_validate, focus=self.on_text_focus)

            def on_text_validate(self, instance):
                self.text = instance.text
                self.edit = False

            def on_text_focus(self, instance, focus):
                if focus is False:
                    self.text = instance.text
                    self.edit = False        
        import csv
        filename = "data.csv"
        fields = []
        col = []          
        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            fields = next(csvreader)
            for field in fields:
                col.append(field)
        
        layout = FloatLayout()
        self.label = Label(text ="Name", 
        color =(1, 0, .65, 1), 
        size_hint = (.4, .1),
        pos_hint = {"x":0.10, "y":0.80}) 
        layout.add_widget(self.label)
        self.labeld = EditableLabel(text =col[0],color =(1, 0, .65, 1),size_hint = (.4, .1),pos_hint = {"x":0.30, "y":0.80})
        layout.add_widget(self.labeld)
        


        self.label1 = Label(text ="Date of Birth", 
        color =(1, 0, .65, 1), 
        size_hint = (.4, .1),
        pos_hint = {"x":0.10, "y":0.70}) 
        layout.add_widget(self.label1)
        self.label1d = EditableLabel(text =col[1],color =(1, 0, .65, 1),size_hint = (.4, .1),pos_hint = {"x":0.30, "y":0.70})
        layout.add_widget(self.label1d)

        self.label2 = Label(text ="Height", 
        color =(1, 0, .65, 1), 
        size_hint = (.4, .1),
        pos_hint = {"x":0.10, "y":0.60}) 
        layout.add_widget(self.label2)
        self.label2d = EditableLabel(text =col[2],color =(1, 0, .65, 1),size_hint = (.4, .1),pos_hint = {"x":0.30, "y":0.60}) 
        layout.add_widget(self.label2d)

        self.label3 = Label(text ="Weight", 
        color =(1, 0, .65, 1), 
        size_hint = (.4, .1),
        pos_hint = {"x":0.10, "y":0.50}) 
        layout.add_widget(self.label3)
        self.label3d = EditableLabel(text =col[3],color =(1, 0, .65, 1),size_hint = (.4, .1),pos_hint = {"x":0.30, "y":0.50}) 
        layout.add_widget(self.label3d)

        self.label4 = Label(text ="Gender", 
        color =(1, 0, .65, 1), 
        size_hint = (.4, .1),
        pos_hint = {"x":0.10, "y":0.40}) 
        layout.add_widget(self.label4)
        self.label4d = EditableLabel(text =col[4],color =(1, 0, .65, 1),size_hint = (.4, .1),pos_hint = {"x":0.30, "y":0.40}) 
        layout.add_widget(self.label4d)
        
        self.label5 = Label(text ="Emergency Contact", 
        color =(1, 0, .65, 1), 
        size_hint = (.4, .1),
        pos_hint = {"x":0.10, "y":0.30}) 
        layout.add_widget(self.label5)
        self.label5d = EditableLabel(text =col[5],color =(1, 0, .65, 1),size_hint = (.4, .1),pos_hint = {"x":0.30, "y":0.30}) 
        layout.add_widget(self.label5d)


        self.update = Button(text ="Update Info", 
        color =(1, 0, .65, 1), 
        size_hint = (.12, .1),
        pos_hint = {"x":0.65, "y":0.30}) 
        def update():
            f = open(filename, "w+")
            f.close()
            fields = [self.labeld.text, self.label1d.text, self.label2d.text, self.label3d.text, self.label4d.text,  self.label5d.text]
            with open(filename, 'w') as csvfile: 
                # creating a csv writer object 
                csvwriter = csv.writer(csvfile) 
                    
                # writing the fields 
                csvwriter.writerow(fields) 
            print(self.labeld.text, self.label1d.text, self.label2d.text, self.label3d.text, self.label4d.text,  self.label5d.text)
        self.update.bind(on_press=lambda x: update())
        layout.add_widget(self.update)

        self.back = Button(text ="BACK", 
        color =(1, 0, .65, 1), 
        size_hint = (.2, .1),
        pos_hint = {"x":0.30, "y":0.10}) 
        def back():
                layout.clear_widgets()
                App().get_running_app().stop()
                import home
                home.home()
        self.back.bind(on_press=lambda x: back())
        layout.add_widget(self.back)


        self.logout = Button(text ="LOGOUT", 
        color =(1, 0, .65, 1), 
        size_hint = (.2, .1),
        pos_hint = {"x":0.60, "y":0.10}) 
        def logoutf():
                layout.clear_widgets()
                App().get_running_app().stop()
                config.conf(2)
        self.logout.bind(on_press=lambda x: logoutf())
        layout.add_widget(self.logout)
        return layout; 

def home():
    SpinnerExample().run()	 
