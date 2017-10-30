'''
AboutScreen:
=============
Display the logo
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from uix.buttons import SocialButton
import json


class AboutScreen(Screen):

    data = ObjectProperty()

    Builder.load_string('''
<AboutScreen>
    name: 'AboutScreen'
    BoxLayout
        orientation: 'vertical'

        orientation: 'vertical'
        TopBar
        BoxLayout:
            orientation: 'vertical'
            padding: dp(20), dp(10)
            canvas:
                Color:
                    rgba: (.91, .91, .91, 1)
                Rectangle:
                    pos: self.pos
                    size: self.size
            AsyncImage
                id: logo
                source: 'data/images/logo.png'
            SocialButton:
                size_hint: 1, .2
                id: website
                social_image: 'data/images/social/website.png'
            Label:
                text: '2nd-3rd Nov, Workshop/Devsprints \\n 4th-5th Nov, Conference Days'
                text_size: self.size
                halign: 'center'
                valign: 'center'
                font_size: dp(24)
                bold: True
                color: 0, 0, 0, 1
            Label:
                id: about
                text: ''
                text_size: self.size
                halign: 'left'
                valign: 'top'
                font_size: dp(22)
                color: 0, 0, 0, 1
    ''')

    def on_pre_enter(self):

        with open('eventsapp/data/jsonfiles/about.json') as data_file:
            data = json.load(data_file)

        data = data.get("0.0.1")[0]

        self.ids.logo.source = data['logo']
        self.ids.website.social_address = data['website']
        self.ids.about.text = data['about']
