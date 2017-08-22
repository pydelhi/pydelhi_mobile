'''
Navigation Screen
=================
Display a Navigation drawer

-------- ----------------------------------
        | =    PyCon India 2017            |
        |__________________________________
        |                                  |
        |                                  |
        |                                  |
But1    |                                  |
        |     Logo Here                    |
But2    |                                  |
        |                                  |
But3    |       ----------------------     |
        |     [ Workshop + Dev Sprints ]   |
But4    |       ----------------------     |
        |                                  |
But5    |       ----------------------     |
        |     [ Conference Days        ]   |
But6    |       ----------------------     |
        |                                  |
        |                                  |
'''


# from kivy.factory import Factory
#Factory.register('NavigationDrawer', module='uix.navigationdrawer')
from uix.navigationdrawer import NavigationDrawer
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

class NavigationScreen(Screen):
    '''
    '''

    Builder.load_string('''
<ImgBut@ButtonBehavior+Image>

<TopBar@BoxLayout>
    size_hint: 1, None
    height: dp(45)
    width: dp(45)
    spacing: dp(15)
    canvas.before:
        Color:
            rgba: 69/255., 132/255., 182/255., 1
        Rectangle:
            size: self.size
            pos: self.pos
    ImgBut
        source: 'data/images/hamburger.png'
        size_hint_x: None
        size_hint_y: 1
        width: self.height
        allow_stretch: True
        on_release: app.navigationdrawer.toggle_state()
    Label:
        text: 'PyCon India 2017'
        text_size: self.size
        halign: 'left'
        valign: 'center'

<BButton@Button>
    border: 10, 10, 10, 10
    background_normal: 'data/images/btn.png'
    background_down: 'data/images/btn.png'
    opacity: 1 if self.state == 'normal' else .9
    size_hint_y: None
    height: dp(45)

<NavigationScreen>
    name: 'NavigationScreen'
    NavigationDrawer
        anim_type: 'slide_above_anim'
        on_parent: if self.parent: app.navigationdrawer = self
        BoxLayout
            orientation: 'vertical'
            Image
            Button
        ScreenManager
            id: nav_manager
            on_parent: if self.parent: app.load_screen('WelcomeScreen', manager=self)


''')