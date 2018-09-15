'''Startup screen
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from uix.behaviors import CoverImage

class StartupScreen(Screen):
    '''
    '''
    Builder.load_string('''
<AsyncImage>
    mipmap: True

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
    active: False
    height: (self.texture_size[1] + dp(9)) if self.text else 0
    backcolor:
        (app.base_active_color[:3] if self.active else\
        app.base_inactive_color[:3]) + [.3]
    color: (.22, .22, .22, 1) if not self.active else (1, 1, 1, 1)
    text_size: self.width - dp(9), None
    halign: 'center'

<LeftAlignedLabel@SingleLineLabel>
    halign: 'left'

<TouchRippleBehavior>
    ripple_color: app.base_active_color

<PyConButton@Background+TouchRippleBehavior+ToggleButtonBehavior+Label>
    text: ''
    size_hint_y: None
    allow_no_selection: False
    height: dp(45)
    backcolor: app.base_active_color if self.state == 'normal' else app.base_inactive_color
    source: 'atlas://data/default/but_light'

<ImBut@TouchRippleBehavior+ButtonBehavior+Image>
    color: app.base_active_color
    text_size: self.size
    size_hint_y: None
    mipmap: True
    height: dp(30)

<ActiveButton@TouchRippleBehavior+ButtonBehavior+Label>
    color: app.base_active_color
    size_hint_y: None
    height: dp(45)
    canvas.before:
        Color:
            rgba: app.base_active_color if self.state == 'normal' else app.base_inactive_color
        RoundedRectangle:
            segments: 20
            size: self.size
            pos: self.pos
        Color:
            rgba: 1, 1, 1, 1
        RoundedRectangle:
            segments: 20
            radius:[(8.0, 8.0), (8.0, 8.0), (8.0, 8.0), (8.0, 8.0)]
            size: self.width - dp(3), self.height - dp(3)
            pos: self.x + dp(1.5), self.y + dp(1.5)


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
    Image
        source: 'data/images/dots.png'
        allow_stretch: True
        keep_ratio: False
        on_parent:
            self.texture.wrap = "repeat"
            self.texture.uvsize = 7, 22
    Image
        id: img_logo
        allow_strech: True
        source: 'atlas://data/default/logo'
        size_hint_y: None

''')
    