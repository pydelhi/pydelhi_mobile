'''
Community Screen:
=============
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from uix.buttons import SocialButton
from uix.cards import CardsContainer, CardStackLayout
import json
from itertools import islice


class CommunityScreen(Screen):

    Builder.load_string('''
<CommunityScreen>
    name: 'CommunityScreen'
    BoxLayout:
        orientation: 'vertical'
        TopBar
        CardsContainer:
            size_hint_y: 1
            CardStackLayout:
                spacing: dp(4)
                AsyncImage
                    id: logo
                    size_hint_y: None
                    height: self.parent.height/3.5
                    source: 'data/images/lg.png'
                Label:
                    id: about
                    text: ''
                    size_hint_y: None
                    height: self.parent.height/2.5
                    text_size: self.size
                    halign: 'center'
                    valign: 'center'
                    font_size: dp(15)
                    color: 0, 0, 0, 1
                GridLayout:
                    cols: 5 if self.width > dp(200) else 3
                    rows: 1 if self.width > dp(200) else 2
                    size_hint_y: None 
                    height: dp(100)
                    id: social_icons
                    padding: dp(20), dp(20)
                    spacing: dp(10), dp(10)
                    
    ''')

    def add_social_icons(self, instance, data):

        for icon, address in data.items():
            social_image = 'data/images/social/{}.png'.format(icon)
            instance.add_widget(SocialButton(social_image=social_image,
                                             social_address=address))

    def on_pre_enter(self):

        with open('eventsapp/data/jsonfiles/community.json') as data_file:
            data = json.load(data_file)

        data = data.get("0.0.1")[0]

        self.ids.logo.source = data['photo']
        self.ids.about.text = data['about']
        social_icons = self.ids.social_icons
        social_icons.clear_widgets()
        self.community_social = data['social']

        def chunks(data, SIZE=10):
            it = iter(data)
            for i in range(0, len(data), SIZE):
                yield {k:data[k] for k in islice(it, SIZE)}

        if self.community_social != []:
            for items in chunks(self.community_social, 3):
                bl = BoxLayout()
                self.add_social_icons(bl, items)
                social_icons.add_widget(bl)
