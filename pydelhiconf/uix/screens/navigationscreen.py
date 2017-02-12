'''Navigation Screen
'''
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from uix.navigationdrawer import NavigationDrawer
from kivy.factory import Factory

Factory.register('TouchRippleBehavior', module='uix.behaviors')


class NavigationScreen(Screen):
  '''
  '''

  Builder.load_string('''
<TouchRippleBehavior>
    ripple_color: app.base_active_color

<MenuButton@TouchRippleBehavior+ToggleButtonBehavior+Background>
    text: ''
    size_hint_y: None
    allow_no_selection: False
    group: 'LeftPanel'
    height: dp(45)
    color: app.base_active_color if self.state == 'normal' else app.base_inactive_color
    source: 'atlas://data/default/but_light'
    on_released: app.navigationdrawer.toggle_state()
    Label:
        size: root.size
        pos: root.pos
        text: root.text

<LeftPanel@BoxLayout+Background>
    source: 'atlas://data/default/bg'
    orientation: 'vertical'
    padding: dp(7), dp(7)
    Image
        source: "atlas://data/default/logo"
        size_hint: 1, None
        height: dp(130)
    ScrollView
        GridLayout
            cols: 1
            size_hint_y: None
            height: self.minimum_height
            MenuButton
                text: 'Schedule'
                on_released: app.load_screen('ScreenSchedule', manager=app.navigation_manager)
            MenuButton
                text: 'Sponsors'
                on_release: app.load_screen('ScreenSponsor', manager=app.navigation_manager)
            MenuButton
                text: 'Venue'
                on_release: app.load_screen('ScreenVenue', manager=app.navigation_manager)
            # MenuButton
            #     text: 'OpenSpaces'
            MenuButton
                text: 'DevSprints'
            MenuButton
                text: 'Ticket'
            MenuButton
                text: 'Community'
            MenuButton
                text: 'About'
            MenuButton
                text: 'Exit'
                on_release: app.stop()

<TopBar@BoxLayout>
    size_hint_y: None
    height: dp(45)
    ImgBut
        source: 'atlas://data/default/hamburger'
        size_hint_x: None
        width: self.height
        on_release: app.navigationdrawer.toggle_state()


<RightPanel@BoxLayout+Background>
    source: 'atlas://data/default/bg'
    orientation: "vertical"
    TopBar
    ScreenManager
        on_parent: app.navigation_manager = nav_sm
        id: nav_sm

<NavigationScreen>
    name: 'NavigationScreen'
    on_enter: app.load_screen('ScreenSchedule', manager=app.navigation_manager)
    NavigationDrawer
        id: navigationdrawer
        on_parent: app.navigationdrawer = navigationdrawer
        LeftPanel
        RightPanel
            opacity: 1-(self.x/root.right)
''')