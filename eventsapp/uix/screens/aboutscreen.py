'''
AboutScreen:
=============
Display the logo
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

class AboutScreen(Screen):

   Builder.load_string('''
<AboutScreen>
    name: 'AboutScreen'
    BoxLayout
        orientation: 'vertical'
        TopBar
        Button
 ''')
