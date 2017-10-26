'''
Speaker Detail Screen:
=====================

'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from uix.tabbedpanels import DateTabbedPanel
import json


class SpeakerDetailScreen(Screen):

    Builder.load_string('''
<SpeakerDetailScreen>
    name: 'SpeakerDetailScreen'
    BoxLayout
        orientation: 'vertical'
        TopBar
        ScheduleCard
 ''')

    def on_enter(self, onsuccess = False):
        with open('eventsapp/data/jsonfiles/tracks.json') as data_file:
            data = json.load(data_file)

        data = data.get("0.0.1")
        print(data)
