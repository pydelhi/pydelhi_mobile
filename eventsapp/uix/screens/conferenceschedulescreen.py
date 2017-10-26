'''
ConferenceScheduleScreen:
=============

'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.scrollview import ScrollView
from uix.tabbedpanels import DateTabbedPanel
from uix.cards import CardsContainer
import json


class ConferenceScheduleScreen(Screen):

    Builder.load_string('''
<ConferenceScheduleScreen>
    name: 'ConferenceScheduleScreen'
    BoxLayout
        orientation: 'vertical'
        TopBar
        DateTabbedPanel
            id: conferencedatedtab
    ''')

    def add_dated_tabs(self, conferencedatedtab, title, halls, data):
        data = data[title]

        dated_tab_item = Factory.DateTabbedPanelItem(text=title)
        hall_tab = Factory.HallTabbedPanel()
        dated_tab_item.add_widget(Factory.HallTabbedPanel())

        for idx, hall_name in enumerate(halls):
            schedule_card = self.add_schedule_cards(idx, data)
            hall = Factory.HallTabbedPanelItem(text=hall_name)

            hall.add_widget(schedule_card)
            hall_tab.add_widget(hall)

        dated_tab_item.add_widget(hall_tab)
        conferencedatedtab.add_widget(dated_tab_item)

    def add_schedule_cards(self, hall_number, data):
        schedule_card_container = CardsContainer(cols=1,
                                                 size_hint_y=None,
                                                 size=(self.size[0], self.parent.size[1]))
        hall_number += 1

        for talk in data:
            hall_id = talk.get('track')
            if (str(hall_id) == str(hall_number)) or (hall_id == 'all'):
                talk_id = talk.get('talk_id')
                talk_title = talk.get('title')
                start_time = talk.get("start_time")
                end_time = talk.get("end_time")
                schedule_card = Factory.ScheduleCard(talk_id=talk_id,
                                                     talk_title=talk_title,
                                                     start_time=start_time,
                                                     end_time=end_time)
                schedule_card_container.add_widget(schedule_card)

        scrollable_cards = Factory.ScrollableCardContainer()
        scrollable_cards.add_widget(schedule_card_container)

        return scrollable_cards

    def on_pre_enter(self, onsuccess = False):
        with open('eventsapp/data/jsonfiles/schedule.json') as data_file:
            data = json.load(data_file)

        data = data.get("0.0.1")[0]
        conferencedatedtab = self.ids.conferencedatedtab
        conferencedatedtab.clear_widgets()

        halls, *days = list(data.keys())
        halls = data[halls]
        for day in days:
            self.add_dated_tabs(conferencedatedtab, day, halls, data)
