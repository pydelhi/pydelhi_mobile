'''
Theme Button:
================

'''

from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, StringProperty
import webbrowser


class ThemeButton(Button):

    background_normal = StringProperty('data/images/btn1.png')
    background_down = StringProperty('data/images/btn1.png')

    Builder.load_string('''
<ThemeButton>:
    font_size: dp(12)
    border: 10, 10, 10, 10
    color: 0, 0, 0, 1
    background_normal: root.background_normal
    background_down: root.background_down
    opacity: 1 if self.state == 'normal' else .9
    ''')
