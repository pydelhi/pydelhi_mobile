from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from functools import partial

app = App.get_running_app()


class SpeakerDetails(Factory.ScrollGrid):

    speaker = ObjectProperty({'Photo': ''})

    Builder.load_string('''
<SpeakerDetails>
    AsyncImage:
        source: root.speaker['photo']
        opacity: 1 if root.speaker['photo']  else 0
        allow_stretch: True
        size_hint_y: None
        height: dp(200)
        mipmap: True
    BackLabel
        active: True
        text: root.speaker['name']
    BackLabel
        text: root.speaker['info']
        ''')


class ScreenTalks(Screen):
    '''
    Screen to display the talk schedule as per talks.json generated by
    pyconf.network every time the app is started. A default
    talk schedule is provided.

    Screen looks like:

    -----------------------------------------
   |              ------------               |
   |              |          |               |
   |              |          |               |
   |              |          |               |
   |              |          |               |
   |              |          |               |
   |              ------------               |
   |              Speaker name               |
   |                                         |
   |About talk                               |
   |                                         |
   |About speaker                            |
   |Social links                             |
   |                                         |
    -----------------------------------------

    '''

    talkid = StringProperty('')

    Builder.load_string('''
#:import do_share utils.do_share
<ScreenTalks>
    spacing: dp(9)
    name: 'ScreenTalks'
    BoxLayout:
        orientation: 'vertical'
        ScrollView
            id: scroll
            ScrollGrid
                id: container
                BackLabel:
                    active: True
                    id: talk_title
                BackLabel:
                    id: talk_desc
        BoxLayout
            size_hint_y: None
            height: dp(54)
            padding: dp(9)
            ImBut
                id: but_share
                data: talk_title.text
                source: 'atlas://data/default/share'
                color: app.base_active_bright[:3] + [.9]
                on_release: do_share(self.data, "PyCon India 2018")
            # ImBut
            #     data: ''
            #     source: 'atlas://data/default/reminder'
            #     color: app.base_active_bright[:3] + [.9]
            ImBut
                source: 'atlas://data/default/feedback'
                color: app.base_active_bright[:3] + [.9]
                on_release:
                    scr = load_screen("ScreenFeedback", manager=root.manager)
                    scr.talk = talk_title.text
        ''')

    def on_pre_enter(self):
        container = self.ids.container
        container.opacity = 0

    def on_enter(self, onsuccess=False):
        container = self.ids.container

        if self.from_back:
            Factory.Animation(opacity=1, d=.3).start(container)
            return

        if len(container.children) > 2:
                container.remove_widget(container.children[0])
        from network import get_data
        talks = get_data('tracks', onsuccess=onsuccess)
        gl = None
        if not talks:
            return
        try:
            talk_info = talks['0.0.1'][0][self.talkid]
        except KeyError:
            # no details for this talk exist...
            # let's go back to previous screen
            from utils import go_back_in_history
            go_back_in_history()
            return

        self.ids.talk_title.text = talk_info['title']
        self.ids.talk_desc.text = talk_info['description']
        if 'speaker' in talk_info.keys():
            speaker = talk_info['speaker']
            if speaker['name']:
                speaker_details = SpeakerDetails(speaker=speaker)
                if 'social' in speaker:
                    speaker_social = speaker['social']
                    items = speaker_social.items()
                    social_len = len(items)
                    gl = GridLayout(cols=social_len, size_hint_y=None,
                                    padding='2dp', spacing='2dp')
                    import webbrowser
                    # update data for share button
                    if 'proposal' in speaker_social:
                        self.ids.but_share.data = "Checkout this talk " \
                            + speaker_social['proposal'] + " by "\
                            + speaker['name']
                    # display social buttons
                    for social_acc, social_link in items:
                        imbt = Factory.ImBut()
                        imbt.source = 'atlas://data/default/' + \
                            social_acc.lower()
                        imbt.bind(on_release = partial(
                            webbrowser.open, social_link))
                        imbt.color = app.base_active_bright[:3] + [.9]
                        gl.add_widget(imbt)
                    speaker_details.add_widget(gl)
                self.ids.container.add_widget(speaker_details)
        Factory.Animation(opacity=1, d=.3).start(container)
        self.ids.scroll.scroll_y = 1
