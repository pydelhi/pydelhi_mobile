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
<LeftAlignedLabel@SingleLineLabel>
    halign: 'left'

<StartupScreen>
    name: 'StartupScreen'
    on_enter:
        from kivy.animation import Animation
        img_logo.opacity=0
        Animation(d=.5, top=self.height/1.5, height=self.height/2, opacity=1).start(img_logo)
        from kivy.clock import Clock
        Clock.schedule_once(lambda dt: app.load_screen('NavigationScreen'), 2)
    Background:
        color: app.base_color
        source: 'atlas://data/default/bg'
    Image
        id: img_logo
        source: 'atlas://data/default/logo'
        size_hint_y: None
''')
    