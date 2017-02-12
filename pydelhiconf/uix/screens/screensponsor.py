'''ScreenSponsor:
Display all the logos of the sponsors.
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

class ScreenSponsor(Screen):
    
    Builder.load_string('''
<ScreenSponsor>
    name: 'ScreenSponsor'
''')