from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

class ScreenFeedback(Screen):
    Builder.load_string('''
<ScreenFeedback>
    name: 'ScreenFeedback'
        ''')