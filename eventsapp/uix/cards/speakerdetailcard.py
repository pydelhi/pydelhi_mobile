'''
Speaker Detail Card:
=============

'''

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.app import App

import webbrowser


class SpeakerDetailCard(BoxLayout):

    speaker_data = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super(SpeakerDetailCard, self).__init__(*args, **kwargs)
        self.speaker_social = self.speaker_data['speaker_social']
        if self.speaker_social != []:
            self.add_social_icons()

    Builder.load_string('''
<SpeakerDetailCard>:
    canvas:
        Color:
            rgba: (.91, .91, .91, 1)
        Rectangle:
            pos: self.pos
            size: self.size
    orientation: 'vertical'
    padding: dp(20), dp(10)
    BoxLayout:
        orientation: 'vertical'
        AsyncImage
            source: root.speaker_data['photo']
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: root.speaker_data['name']
                size_hint: 1, .5
                text_size: self.size
                halign: 'left'
                valign: 'center'
                font_size: dp(22)
                bold: True
                color: 0, 0, 0, 1
            Label:
                text: root.speaker_data['info']
                text_size: self.size
                halign: 'left'
                valign: 'top'
                font_size: dp(18)
                color: 0, 0, 0, 1
        BoxLayout:
            id: social_icons
            size_hint: 1, .4
            padding: dp(10), dp(15)

    ''')

    def add_social_icons(self):

        social_icons = self.ids.social_icons
        social_icons.clear_widgets()

        for icon, address in self.speaker_social[0].items():
            social_image = 'data/images/social/{}.png'.format(icon)
            social_icons.add_widget(SocialButton(social_image=social_image,
                                                 social_address=address))


class SocialButton(ButtonBehavior, Image):

    social_image = StringProperty('data/images/social/github.png')
    social_address = StringProperty('')

    def on_release(self):
        webbrowser.open_new(self.social_address)

    Builder.load_string('''
<SocialButton>:
    source: root.social_image
    width: self.height
    allow_stretch: True
    ''')
