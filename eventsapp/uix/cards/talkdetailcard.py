'''
Talk Detail Card:
=============

'''

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty
from kivy.app import App


class TalkDetailCard(ButtonBehavior, BoxLayout):

    talk_id = StringProperty()
    talk_title = StringProperty()
    start_time = StringProperty()
    end_time = StringProperty()
    navigate_to = StringProperty('SpeakerDetailScreen')

    def __init__(self, *args, **kwargs):
        super(TalkDetailCard, self).__init__(*args, **kwargs)


    Builder.load_string('''
<TalkDetailCard>:
    canvas:
        BorderImage:
            source: 'data/images/card.png'
            pos: self.pos
            size: self.size
    orientation: 'vertical'
    padding: dp(20), dp(10)
    size_hint_y: None
    size: self.size[0], 250
    on_release: app.load_screen(root.navigate_to, manager=app.navigation_screen.ids.nav_manager)
    Label:
        text: 'Time: {} to {}'.format(root.start_time, root.end_time)
        size_hint: 1, .5
        text_size: self.size
        halign: 'left'
        valign: 'center'
        font_size: dp(18)
        bold: True
        color: 0, 0, 0, 1
    Label:
        text: root.talk_title
        text_size: self.size
        halign: 'left'
        valign: 'top'
        font_size: dp(18)
        bold: True
        color: 0, 0, 0, 1
    ''')
