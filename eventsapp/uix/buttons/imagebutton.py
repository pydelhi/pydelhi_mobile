'''
Image Button:
================

'''

from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import ObjectProperty, StringProperty
import webbrowser


class ImageButton(ButtonBehavior, Image):

    back_button_image = StringProperty('')

    Builder.load_string('''
<ImageButton>:
    source: root.back_button_image
    size_hint_x: None
    size_hint_y: 1
    width: self.height
    allow_stretch: True
    ''')
