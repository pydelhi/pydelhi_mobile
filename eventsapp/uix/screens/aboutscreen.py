'''
AboutScreen:
=============
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from uix.cards import CardsContainer, CardBoxLayout
from uix.buttons import SocialButton
import json
from itertools import islice


class AboutScreen(Screen):

    Builder.load_string('''
<AboutScreen>
    name: 'AboutScreen'
    BoxLayout:
        orientation: 'vertical'
        TopBar
        CardsContainer:
            size_hint_y: 1
            CardBoxLayout:
                AsyncImage
                    id: logo
                    source: 'data/images/logo.png'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: dp(20)
                    size_hint_y: None
                    size: self.size[0], dp(150)
                    id: social_icons
                    padding: dp(10), dp(15)
                Label:
                    text: '2nd-3rd Nov, Workshop/Devsprints \\n 4th-5th Nov, Conference Days'
                    text_size: self.size
                    halign: 'center'
                    valign: 'center'
                    font_size: dp(16)
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

                    
 '''
    )
    def add_social_icons(self, instance, data):
    
        for icon, address in data.items():
            social_image = 'data/images/social/{}.png'.format(icon)
            instance.add_widget(SocialButton(social_image=social_image,
                                             social_address=address))

    def on_pre_enter(self):

        with open('eventsapp/data/jsonfiles/about.json') as data_file:
            data = json.load(data_file)

        data = data.get("0.0.2")[0]

        self.ids.logo.source = data['logo']
        # self.ids.website.social_address = data['website']
        self.ids.about.text = data['about']
        social_icons = self.ids.social_icons
        social_icons.clear_widgets()
        self.community_social = data['social']

        # self.ids.facebook.social_address = data['social']['facebook']
        def chunks(data, SIZE=10):
            it = iter(data)
            for i in range(0, len(data), SIZE):
                yield {k:data[k] for k in islice(it, SIZE)}

        if self.community_social != []:
            for items in chunks(self.community_social, 3):
                bl = BoxLayout()
                self.add_social_icons(bl, items)
                social_icons.add_widget(bl)

