'''
Schedule Cards Container:
================

'''

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from uix.schedulecards import ScheduleCard


class ScheduleCardsContainer(BoxLayout):
    Builder.load_string('''
<ScheduleCardsContainer>:
    orientation: 'vertical'
    spacing: dp(10)
    padding: dp(20), dp(40)
    canvas:
        Color:
            rgba: (1, 1, 1, 1)
        Rectangle:
            size: self.size
            pos: self.pos
    ScheduleCard
    ScheduleCard
    ScheduleCard
    ''')
