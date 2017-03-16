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
    backcolor: app.base_color
    canvas.before:
        Color:
            rgba: root.backcolor if root.backcolor else (1, 1, 1, 1)
        Rectangle:
            source: root.source
            size: self.size
            pos: self.pos

<ScrollGrid@GridLayout>
    id: container
    cols: 1
    size_hint_y: None
    padding: '9dp'
    spacing: '9dp'
    height: self.minimum_height

<BackLabel@Background+Label>
    valign: 'middle'
    size_hint_y: None
    height: (self.texture_size[1] + dp(9)) if self.text else 0
    backcolor: app.base_active_bright[:3] +  [0.5]
    text_size: self.width - dp(9), None   
    halign: 'center'    

<LeftAlignedLabel@SingleLineLabel>
    halign: 'left'

<TouchRippleBehavior>
    ripple_color: app.base_active_color

<PyConButton@TouchRippleBehavior+ToggleButtonBehavior+Background>
    text: ''
    size_hint_y: None
    allow_no_selection: False
    height: dp(45)
    backcolor: app.base_active_color if self.state == 'normal' else app.base_inactive_color
    source: 'atlas://data/default/but_light'
    Label:
        size: root.size
        pos: root.pos
        text: root.text

<ImBut@TouchRippleBehavior+ButtonBehavior+Image>
    text_size: self.size
    size_hint_y: None
    mipmap: True
    height: dp(30)

<ActiveButton@PyConButton>
    source: ''

<AsyncImage>
    anim_delay: .05

<StartupScreen>
    name: 'StartupScreen'
    on_enter:
        from kivy.animation import Animation
        img_logo.opacity=0
        Animation(d=.5, top=self.height/1.3, height=self.height/2., width = self.width, opacity=1).start(img_logo)
        from kivy.clock import Clock
        Clock.schedule_once(lambda dt: app.load_screen('NavigationScreen'), 1)
    Background:
        backcolor: app.base_color
        source: 'atlas://data/default/bg'
    Image
        id: img_logo
        allow_strech: True
        source: 'atlas://data/default/logo'
        size_hint_y: None

''')
    