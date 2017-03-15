from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from functools import partial

import webbrowser


class ScreenAbout(Screen):
    Builder.load_string('''
<ScreenAbout>
    spacing: dp(9)
    name: 'ScreenAbout'
    ScrollView
        id: scroll
        ScrollGrid
            id: container
            AsyncImage
                id: imgbt
                size_hint_y: None
                height: dp(200)
            BackLabel
                id: comm_desc
        ''')

    def on_enter(self, onsuccess=False):
        from network import get_data
        about = get_data('about', onsuccess=onsuccess)

        if not about:
            return

        about = about.get('0.0.1')[0]
        imbt = self.ids.imgbt
        imbt.source = about['logo']

        self.ids.comm_desc.text = about['about']