'''
Community Screen:
=============
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from uix.buttons import SocialButton
import json
from itertools import islice


class CommunityScreen(Screen):

    Builder.load_string('''
<CommunityScreen>
    name: 'CommunityScreen'
    BoxLayout
        orientation: 'vertical'
        TopBar
        StackLayout:
            pos: self.parent.pos
            size: self.parent.size
            orientation: 'lr-tb'

            padding: dp(20), dp(10)
            spacing: dp(40)
            canvas:
                Color:
                    rgba: (.91, .91, .91, 1)
                Rectangle:
                    pos: self.pos
                    size: self.size
            AsyncImage
                id: logo
                size_hint_y: None
                height: self.parent.height/4
                source: 'data/images/logo.png'
            Label:
                id: about
                text: ''
                size_hint_y: None
                height: self.parent.height/4
                text_size: self.size
                halign: 'center'
                valign: 'center'
                font_size: dp(20)
                color: 0, 0, 0, 1
            BoxLayout:
                orientation: 'vertical'
                spacing: dp(20)
                size_hint_y: None
                size: self.size[0], dp(150)
                id: social_icons
                padding: dp(10), dp(15)
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
