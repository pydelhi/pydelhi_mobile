'''
Schedule Card:
=============

'''

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior


class ScheduleCard(BoxLayout, ButtonBehavior):
    Builder.load_string('''
<ScheduleCard>:
    canvas:
        BorderImage:
            source: 'data/images/card.png'
            pos: self.pos
            size: self.size
    orientation: 'vertical'
    padding: dp(20), dp(10)
    Label:
        text: 'Time: 08:00 to 09:00'
        size_hint: 1, .5
        text_size: self.size
        halign: 'left'
        valign: 'center'
        font_size: dp(18)
        bold: True
        color: 0, 0, 0, 1
    Label:
        text: 'Registration & Breakfast'
        text_size: self.size
        halign: 'left'
        valign: 'top'
        font_size: dp(18)
        bold: True
        color: 0, 0, 0, 1

    ''')
