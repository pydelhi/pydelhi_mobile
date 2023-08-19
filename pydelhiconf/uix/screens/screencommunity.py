from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.factory import Factory
from kivy.lang import Builder
from functools import partial


class ScreenCommunity(Screen):
    Builder.load_string('''
<ScreenCommunity>
    name: 'ScreenCommunity'
    ScrollView
        id: main
        ScrollGrid
            AsyncImage
                id: aimg
                size_hint_y: None
                allow_stretch: True
                height: dp(120)
            BackLabel
                id: bcklbl
            GridLayout
                id: container
                row: 2
                cols: 4
                size_hint_y: None
                padding: '9dp'
                spacing: '9dp'
        ''')

    def on_pre_enter(self):
        self.ids.main.opacity=0

    def on_enter(self, onsuccess=False):
        from network import get_data
        community = get_data('community', onsuccess=onsuccess)

        if not community:
            return

        community = community.get('0.0.1')[0]

        self.ids.bcklbl.text = community['about']
        self.ids.aimg.source = community['photo']

        social_comm = community['social']
        social_len = len(social_comm)

        gl = self.ids.container
        gl.clear_widgets()
        import webbrowser
        for social_acc, social_link in social_comm.items():
            imbt = Factory.ImBut()
            imbt.source = 'atlas://data/default/' + social_acc.lower()
            imbt.on_released = partial(webbrowser.open, social_link)
            gl.add_widget(imbt)

        Factory.Animation(opacity=1, d=.5).start(self.ids.main)