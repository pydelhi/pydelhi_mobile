'''
Speaker Detail Screen:
=====================

'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.factory import Factory
from uix.cards import CardsContainer
import json


class SpeakerDetailScreen(Screen):

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

    def add_speaker_details(self, speaker_container, speaker_name, speaker_info, speaker_image, speaker_social):
        speaker_detail_card = Factory.SpeakerDetailCard(speaker_name=speaker_name,
                                                        speaker_info=speaker_info,
                                                        speaker_image=speaker_image,
                                                        speaker_social=speaker_social)
        speaker_container.add_widget(speaker_detail_card)

    def add_talk_details(self, speaker_container, talk_title, talk_description, talk_type):
        talk_detail_card = Factory.TalkDetailCard(size_hint=(1, .75), 
                                                  talk_title=talk_title,
                                                  talk_description=talk_description,
                                                  talk_type=talk_type)
        speaker_container.add_widget(talk_detail_card)

    def load_data(self):
        with open('eventsapp/data/jsonfiles/tracks.json') as data_file:
            data = json.load(data_file)

        data = data.get("0.0.1")[0].get('07')
        return data

    def on_pre_enter(self, onsuccess = False):
        data = self.load_data()

        talk_title = data.get('title')
        talk_description = data.get('description')
        talk_type = data.get('type')

        speaker = data.get('speaker')
        speaker_name = speaker.get('name')
        speaker_info = speaker.get('info')
        speaker_image = speaker.get('photo')
        speaker_social = speaker.get('social')
        if speaker_social == None:
            speaker_social = []

        speaker_container = self.ids.speaker_container
        speaker_container.clear_widgets()

        self.add_speaker_details(speaker_container,
                                 speaker_name,
                                 speaker_info,
                                 speaker_image,
                                 speaker_social)
        self.add_talk_details(speaker_container,
                              talk_title,
                              talk_description,
                              talk_type)
