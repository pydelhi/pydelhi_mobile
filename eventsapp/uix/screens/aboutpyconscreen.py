'''
About Pycon Screen
===========
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from uix.cards import CardsContainer, CardBoxLayout, CardStackLayout
from uix.buttons import SocialButton
import json


class AboutPyConScreen(Screen):

    Builder.load_string('''
<AboutPyConScreen>
    name: 'AboutPyConScreen'
    BoxLayout:
        orientation: 'vertical'
        TopBar:
            title: 'History'
        CardsContainer:
            size_hint_y: 1
            CardBoxLayout:	
                AsyncImage
                    id: logo
                    source: 'data/images/social/pylogo.png'
                Label:
                    id: about
                    text: ''
                    text_size: self.size
                    halign: 'left'
                    valign: 'top'
                    font_size: dp(15)
                    color: 0, 0, 0, 1
                AsyncImage
                    id: new
                    source: 'data/images/social/pylogo.png'
    ''')

    def on_pre_enter(self):

        with open('eventsapp/data/jsonfiles/history.json') as data_file:
            data = json.load(data_file)

        data = data.get("0.0.1")[0]

        self.ids.logo.source = data['logo']
        
        self.ids.about.text = data['about']

