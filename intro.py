from kivy.uix.floatlayout import FloatLayout
from kivy.uix.sreenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.base import runTouchApp
from kivy.app import App
from kivy.uix.button import Button

class ActivityNote(Screen):
    def __init__(self, **kwargs):
        super(ActivityNote, self).__init__(**kwargs)
        #self.size_hint=(1, 1)
        self.background ='images/effect.png' #'images/effect_empty.png' #'images/new_back.png' #
        box = FloatLayout()
        box.add_widget(Image(source='images/tab_rotate.gif',pos_hint={'center_x':.5,'center_y':.4},size_hint=(.9,.9)))
        box.add_widget(Label(text='Loading... Please Wait...',pos_hint={'center_x':.5,'center_y':.2},size_hint=(.5,.5)))
        self.add_widget(box)
        #self.open()

class ea(App):
    def build(self):
        print('herer')
        return Button(text='hell')
#runTouchApp(ActivityNote())
ea().run()