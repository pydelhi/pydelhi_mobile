'''
ConferenceScheduleScreen:
=============

'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from uix.tabbedpanels import DateTabbedPanel


class ConferenceScheduleScreen(Screen):

    Builder.load_string('''
<ConferenceScheduleScreen>
    name: 'ConferenceScheduleScreen'
    BoxLayout
        orientation: 'vertical'
        TopBar
        DateTabbedPanel
 ''')
