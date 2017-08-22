'''
Welcome Screen
==============
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


class WelcomeScreen(Screen):
    '''
    '''

    Builder.load_string('''
<WelcomeScreen>
    name: 'WelcomeScreen'
    BoxLayout
        orientation: 'vertical'
        TopBar
        RelativeLayout
            Image
                source: 'data/images/navback.png'
                allow_stretch: True
                keep_ratio: False
            Image
                source: 'data/images/overlay.png'
                allow_stretch: True
                keep_ratio: False
            BoxLayout
                orientation: 'vertical'
                Label
                    text: 'Welcome to\\n PyCon India 2017'
                    text_size: self.size
                    valign: 'center'
                    halign: 'center'
                    font_size: dp(18)
                    color: 0, 0, 0, 1
                    bold: True
                BoxLayout
                    orientation: 'vertical'
                    padding: dp(50)
                    spacing: dp(45)
                    BButton
                        text: 'Workshop & DevSprints'
                    BButton
                        text: 'Conference Days'
''')