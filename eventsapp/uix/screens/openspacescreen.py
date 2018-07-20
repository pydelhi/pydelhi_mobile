'''
Open Space Screen:
=============
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from uix.buttons import SocialButton
from uix.cards import CardsContainer, CardBoxLayout
import json


class OpenSpaceScreen(Screen):

    Builder.load_string('''
<OpenSpaceScreen>
    name: 'OpenSpaceScreen'
    BoxLayout
        orientation: 'vertical'
        TopBar
        CardsContainer:
            size_hint_y: 1
            CardBoxLayout:
                spacing: dp(10)
                AsyncImage
                    id: logo
                    size_hint: 1, .7
                    source: 'data/images/logo.png'
                BoxLayout:
                    canvas.before:
                        Color:
                            rgba: (.81, .81, .81, 1)
                        Rectangle:
                            pos: self.pos
                            size: self.size
                    orientation: 'vertical'
                    padding: dp(0), dp(5)
                    Label:
                        id: quote
                        text: ''
                        text_size: self.size
                        halign: 'center'
                        valign: 'top'
                        font_size: dp(10)
                        bold: True
                        color: 0, 0, 0, 1
                    Label:
                        size_hint: 1, .7
                        id: author
                        text: 'Michael M Pannwitz, Open Space practitioner'
                        text_size: self.size
                        halign: 'center'
                        valign: 'center'
                        font_size: dp(8)
                        bold: True
                        color: 0, 0, 0, 1
                Label:
                    id: about
                    text: ''
                    text_size: self.size
                    halign: 'center'
                    valign: 'top'
                    font_size: dp(10)
                    color: 0, 0, 0, 1
    ''')

    def on_pre_enter(self):

        with open('eventsapp/data/jsonfiles/openspace.json') as data_file:
            data = json.load(data_file)

        data = data.get("0.0.1")[0]

        self.ids.logo.source = data['logo']
        self.ids.quote.text = data['quote']
        self.ids.author.text = '- {}'.format(data['author'])
        self.ids.about.text = data['about']
