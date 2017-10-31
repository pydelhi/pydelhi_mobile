'''
Sponsor Detail Card:
=============

'''

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivy.uix.image import Image
from kivy.factory import Factory
from kivy.uix.behaviors import ButtonBehavior
from kivy.app import App

import webbrowser


class SponsorDetailCard(BoxLayout):

    data = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super(SponsorDetailCard, self).__init__(*args, **kwargs)


    Builder.load_string('''
<SponsorDetailCard>:
    canvas:
        Color:
            rgba: (.91, .91, .91, 1)
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [dp(10)]
        Color:
            rgba: (0, 0, 0, 1)
            a: 1
        Line:
            rounded_rectangle: (self.pos[0],self.pos[1],self.size[0],self.size[1], 10)
    orientation: 'vertical'
    padding: dp(10), dp(10)
    size_hint_y: None
    size: self.size[0], dp(500)
    BoxLayout:
        orientation: 'vertical'
        AsyncImage
            source: root.data['logo']
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: root.data['name']
                text_size: self.size
                halign: 'left'
                valign: 'center'
                font_size: dp(22)
                bold: True
                color: 0, 0, 0, 1
            Label:
                text: root.data['about']
                text_size: self.size
                halign: 'left'
                valign: 'top'
                font_size: dp(18)
                color: 0, 0, 0, 1
        BoxLayout:
            id: social_icons
            size_hint: 1, .4
            padding: dp(10), dp(15)
            SocialButton:
                social_image: 'data/images/social/website.png'
                social_address: root.data['website']
            Label:
                text: root.data['type']
                text_size: self.size
                halign: 'center'
                valign: 'center'
                font_size: dp(18)
                bold: True
                color: 0, 0, 0, 1

    ''')
