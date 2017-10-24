'''
WorkshopScheduleScreen:
=====================

'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from uix.tabbedpanels import DateTabbedPanel


class WorkshopScheduleScreen(Screen):

    Builder.load_string('''
<WorkshopScheduleScreen>
    name: 'WorkshopScheduleScreen'
    BoxLayout
        orientation: 'vertical'
        TopBar
        DateTabbedPanel
 ''')
