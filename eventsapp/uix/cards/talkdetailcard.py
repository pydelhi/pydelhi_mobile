'''
Talk Detail Card:
=============

'''

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.app import App


class TalkDetailCard(BoxLayout):

    talk_title = StringProperty("")
    talk_description = StringProperty("")
    talk_type = StringProperty("")

    def __init__(self, *args, **kwargs):
        super(TalkDetailCard, self).__init__(*args, **kwargs)


    Builder.load_string('''
<TalkDetailCard>:
    canvas:
        Color:
            rgba: (.91, .91, .91, 1)
        Rectangle:
            pos: self.pos
            size: self.size
    orientation: 'vertical'
    padding: dp(20), dp(10)
    Label:
        text: root.talk_title
        size_hint: 1, .5
        text_size: self.size
        halign: 'left'
        valign: 'center'
        font_size: dp(22)
        bold: True
        color: 0, 0, 0, 1
    Label:
        text: root.talk_description
        text_size: self.size
        halign: 'left'
        valign: 'top'
        font_size: dp(18)
        color: 0, 0, 0, 1
    Label:
        text: root.talk_type
        size_hint: 1, .5
        text_size: self.size
        halign: 'left'
        valign: 'center'
        font_size: dp(22)
        bold: True
        color: 0, 0, 0, 1
    ''')
