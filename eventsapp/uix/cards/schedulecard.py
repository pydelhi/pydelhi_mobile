'''
Schedule Card:
=============

'''

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty
from kivy.app import App


class ScheduleCard(ButtonBehavior, BoxLayout):

    talk_id = StringProperty("")
    talk_title = StringProperty("")
    start_time = StringProperty("")
    end_time = StringProperty("")
    navigate_to = StringProperty('SpeakerDetailScreen')

    def __init__(self, *args, **kwargs):
        super(ScheduleCard, self).__init__(*args, **kwargs)

    def on_release(self):
        app = App.get_running_app()
        manager = app.navigation_screen.ids.nav_manager
        src = app.load_screen(self.navigate_to, manager=manager)
        src.talk_id = self.talk_id

    Builder.load_string('''
<ScheduleCard>:
    canvas:
        BorderImage:
            source: 'data/images/card.png'
            pos: self.pos
            size: self.size
    orientation: 'vertical'
    padding: dp(20), dp(10)
    size_hint_y: None
    size: self.size[0], 250
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
