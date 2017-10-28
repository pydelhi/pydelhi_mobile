'''
Sponsor Screen
==============
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.properties import StringProperty, ObjectProperty
from uix.cards import SponsorDetailCard, CardsContainer
import json


class SponsorScreen(Screen):

    Builder.load_string('''
<SponsorScreen>
    name: 'SponsorScreen'
    BoxLayout
        orientation: 'vertical'
        TopBar:
            title: 'Sponsors'
        BoxLayout:
            id: sponsor_container
            canvas:
                Color:
                    rgba: (1, 1, 1, 1)
                Rectangle:
                    pos: self.pos
                    size: self.size
            orientation: 'vertical'
            spacing: dp(15)
            padding: dp(20), dp(20)
    ''')


    def load_data(self):
        with open('eventsapp/data/jsonfiles/sponsors.json') as data_file:
            data = json.load(data_file)

        data = data.get("0.0.1")
        return data

    def on_enter(self):
        sponsors = self.load_data()
        sponsor_container = self.ids.sponsor_container
        sponsor_container.clear_widgets()

        schedule_card_container = CardsContainer(cols=1,
                                                 size_hint_y=None,
                                                 size=(self.size[0], self.parent.size[1]))

        def get_valid_value(data, *value):
            details = {}
            for v in value:
                try:
                    val = data.get(v)
                    if val == None:
                        details[v] = ""
                    details[v] = val
                except:
                    details[v] = ""
            return details

        scrollable_cards = Factory.ScrollableCardContainer()
        for sponsor in sponsors:
            data = get_valid_value(sponsor, 'name', 'type', 'website', 'logo', 'about')
            speaker_detail_card = Factory.SponsorDetailCard(data=data)
            scrollable_cards.add_widget(speaker_detail_card)

        sponsor_container.add_widget(scrollable_cards)
