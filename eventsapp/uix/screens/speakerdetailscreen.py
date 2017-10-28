'''
Speaker Detail Screen:
=====================

'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.properties import StringProperty, ObjectProperty
from uix.cards import CardsContainer
import json


class SpeakerDetailScreen(Screen):

    talk_id = StringProperty('')

    Builder.load_string('''
<SpeakerDetailScreen>
    name: 'SpeakerDetailScreen'
    BoxLayout
        orientation: 'vertical'
        TopBar:
            navigate_back: True
            back_button_image: 'data/images/back_button.png'
        BoxLayout:
            id: speaker_container
            canvas:
                Color:
                    rgba: (1, 1, 1, 1)
                Rectangle:
                    pos: self.pos
                    size: self.size
            orientation: 'vertical'
            spacing: dp(15)
            padding: dp(20), dp(20)
 ''')

    def load_data(self):
        with open('eventsapp/data/jsonfiles/tracks.json') as data_file:
            data = json.load(data_file)

        if self.talk_id:
            data = data.get("0.0.1")[0].get(self.talk_id)
            return data

    def on_pre_enter(self):
        speaker_container = self.ids.speaker_container

    def on_enter(self, onsuccess = False):
        data = self.load_data()
        speaker_container = self.ids.speaker_container
        speaker_container.clear_widgets()

        def get_valid_value(data, *value):
            details = {}
            for v in value:
                try:
                    val = data.get(v)
                    if val == None:
                        details[v] = ""
                    details[v] = val
                except:
                    details[v] = ""
            return details

        talk_data = get_valid_value(data, 'title', 'description', 'type')
        speaker = data.get('speaker')
        speaker_data = get_valid_value(speaker, 'name', 'info', 'photo')
        speaker_social = [] if speaker.get('social') == None else speaker.get('social')
        speaker_data['speaker_social'] = speaker_social

        speaker_detail_card = Factory.SpeakerDetailCard(speaker_data=speaker_data)
        talk_detail_card = Factory.TalkDetailCard(size_hint=(1, .75), talk_data=talk_data)

        speaker_container.add_widget(speaker_detail_card)
        speaker_container.add_widget(talk_detail_card)
