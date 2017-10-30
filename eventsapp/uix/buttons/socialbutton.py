'''
Social Button:
================

'''

from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import ObjectProperty, StringProperty
import webbrowser


class SocialButton(ButtonBehavior, Image):

    social_image = StringProperty('')
    social_address = StringProperty('')

    def on_release(self):
        webbrowser.open_new(self.social_address)

    Builder.load_string('''
<SocialButton>:
    source: root.social_image
    width: self.height
    allow_stretch: True
    ''')
