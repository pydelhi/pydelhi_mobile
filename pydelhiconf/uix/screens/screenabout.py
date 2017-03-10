from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

class ScreenAbout(Screen):
	Builder.load_string('''
<ScreenAbout>
    name: 'ScreenAbout'
        ''')