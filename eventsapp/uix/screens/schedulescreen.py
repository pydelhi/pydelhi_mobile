'''
ScheduleScreen:
=============

'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.button import Button
from kivy.properties import OptionProperty
from kivy.uix.scrollview import ScrollView
from uix.tabbedpanels import DateTabbedPanel
from uix.cards import CardsContainer
from kivy.app import App
import json


class ScheduleScreen(Screen):

    Builder.load_string('''
<ScheduleScreen>
    name: 'ScheduleScreen'
    BoxLayout
        orientation: 'vertical'
        TopBar
        BoxLayout:
            id: scheduletab
    ''')

    def add_dated_tabs(self, scheduledatedtab, title, halls, data):
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
        scheduledatedtab.add_widget(dated_tab_item)

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

    def on_enter(self):
        '''
        This is done to handle to create an effect of going back from SpeakerDetailScreen
        to ScheduleScreen.
        '''
        app = App.get_running_app()
        manager = app.navigation_screen.ids.nav_manager
        manager.transition.direction = 'left'

    def on_pre_enter(self):

        with open('eventsapp/data/jsonfiles/schedule.json') as data_file:
            data = json.load(data_file)

        data = data.get("0.0.1")[0]
        scheduletab = self.ids.scheduletab
        app = App.get_running_app()

        if scheduletab.children:
            scheduledatedtab = scheduletab.children[0]
        else:
            scheduledatedtab = Factory.DateTabbedPanel()
            scheduletab.add_widget(scheduledatedtab)

        halls, *days = list(data.keys())
        halls = data[halls]
        for day in days:
            self.add_dated_tabs(scheduledatedtab, day, halls, data)
