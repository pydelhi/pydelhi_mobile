'''Startup screen
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


class StartupScreen(Screen):
    '''
    '''
    Builder.load_string('''
<SingleLineLabel@Label>
    text_size: self.size
    size_hint_y: None
    height: '45dp'
<Background@Widget>
    source: ''
    color: app.base_color
    canvas.before:
        Color:
            rgba: root.color if root.color else (1, 1, 1, 1)
        Rectangle:
            source: root.source
            size: self.size
            pos: self.pos


<StartupScreen>
    name: 'StartupScreen'
    on_enter:
        from kivy.animation import Animation
        Animation(d=.5, width=self.width, top=self.height, height=self.height/2).start(img_logo)
        Animation(d=.5, width=self.width, top=self.height/2, height=self.height/2).start(img_venue)
        from kivy.clock import Clock
        Clock.schedule_once(lambda dt: app.load_screen('NavigationScreen'), 2)
    Background:
        color: app.base_color
        source: 'atlas://data/default/bg'
    Image
        id: img_venue
        source: 'atlas://data/default/venue'
        size_hint_y: None
    Image
        id: img_logo
        source: 'atlas://data/default/logo'
        size_hint_y: None
''')
    