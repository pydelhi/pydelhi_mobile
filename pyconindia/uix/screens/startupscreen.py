'''Startup screen
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


class StartupScreen(Screen):
    '''
    '''
    Builder.load_string('''
<StartupScreen>
    name: 'StartupScreen'
    on_enter:
        from kivy.animation import Animation
        Animation(d=.5, width=self.width, top=self.height, height=self.height/2).start(img_logo)
        Animation(d=.5, width=self.width, top=self.height/2, height=self.height/2).start(img_venue)
        from kivy.clock import Clock
        Clock.schedule_once(lambda dt: app.load_screen('NavigationScreen'), 2)
    Image:
        source: 'atlas://data/default/bg'
        allow_stretch: True
        keep_ratio: False
    Image
        id: img_venue
        source: 'atlas://data/default/venue'
        size_hint_y: None
    Image
        id: img_logo
        source: 'atlas://data/default/logo'
        size_hint_y: None
''')
    