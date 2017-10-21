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
from kivy.properties import (ObjectProperty, NumericProperty, OptionProperty,
                             BooleanProperty, StringProperty)
from kivy.uix.button import Button
from kivy.lang import Builder


class NavButton(Button):
    button_text = StringProperty('')
    icon_source = StringProperty('')


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

<NavButton>
    background_normal: ''
    StackLayout:
        pos: self.parent.pos
        size: self.parent.size
        orientation: 'lr-tb'
        Image:
            source: root.icon_source
            size_hint_x: None
            width: 0.4*self.parent.width
        Label:
            size_hint_x: None
            text: root.button_text
            text_size: dp(150), None
            halign: 'left'
            valign: 'center'
            font_size: dp(18)
            bold: True
            color: 0, 0, 0, 1

<LeftPanel@BoxLayout>
    orientation: 'vertical'
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos
    Image
        id: img_back
        source: "data/images/background.png"
        allow_stretch: True
        keep_ratio: False
        size_hint: 1, None
        height: max(dp(250), 0.25*self.parent.height)
        Image
            source: 'data/images/logo.png'
            size: img_back.width, img_back.height/3.
            center: img_back.center

    RelativeLayout
        size_hint: 1, 1
        BoxLayout
            size_hint: 1, .8
            pos_hint: {'center_y': .55}
            orientation: 'vertical'
            NavButton
                button_text: 'Schedule'
                icon_source: 'data/images/menu/calendar.png'
                on_release:
                    app.navigation_screen.ids.drawer.toggle_state()
                    app.load_screen('AboutScreen', manager=app.navigation_screen.ids.nav_manager)
            NavButton
                button_text: 'About'
                icon_source: 'data/images/menu/about.png'
                on_release:
                    app.navigation_screen.ids.drawer.toggle_state()
                    app.load_screen('AboutScreen', manager=app.navigation_screen.ids.nav_manager)
            NavButton
                button_text: 'Community'
                icon_source: 'data/images/menu/community.png'
                on_release:
                    app.navigation_screen.ids.drawer.toggle_state()
                    app.load_screen('AboutScreen', manager=app.navigation_screen.ids.nav_manager)
            NavButton
                button_text: 'Venue'
                icon_source: 'data/images/menu/venue.png'
                on_release:
                    app.navigation_screen.ids.drawer.toggle_state()
                    app.load_screen('AboutScreen', manager=app.navigation_screen.ids.nav_manager)
            NavButton
                button_text: 'Ticket'
                icon_source: 'data/images/menu/ticket.png'
                on_release:
                    app.navigation_screen.ids.drawer.toggle_state()
                    app.load_screen('AboutScreen', manager=app.navigation_screen.ids.nav_manager)
            NavButton
                button_text: 'Open Source'
                icon_source: 'data/images/menu/community.png'
                on_release:
                    app.navigation_screen.ids.drawer.toggle_state()
                    app.load_screen('AboutScreen', manager=app.navigation_screen.ids.nav_manager)
            NavButton
                button_text: 'Sponsors'
                icon_source: 'data/images/menu/sponsor.png'
                on_release:
                    app.navigation_screen.ids.drawer.toggle_state()
                    app.load_screen('AboutScreen', manager=app.navigation_screen.ids.nav_manager)

<NavigationScreen>
    name: 'NavigationScreen'
    on_parent: app.navigation_screen = self
    NavigationDrawer
        id: drawer
        anim_type: 'slide_above_simple'
        separator_image_width: dp(0)
        side_panel_width: max(dp(350), 0.8*self.width)
        on_parent: if self.parent: app.navigationdrawer = self
        LeftPanel
        ScreenManager
            id: nav_manager
            on_parent: if self.parent: app.load_screen('WelcomeScreen', manager=self)


''')
