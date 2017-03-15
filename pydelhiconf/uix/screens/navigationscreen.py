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
#:import WipeTransition kivy.uix.screenmanager.WipeTransition


<MenuButton@PyConButton>
    group: 'LeftPanel'
    on_released: app.navigationdrawer.toggle_state()

<LeftPanel@BoxLayout+Background>
    source: 'atlas://data/default/bg'
    orientation: 'vertical'
    padding: dp(7), dp(7)
    Image
        source: "atlas://data/default/logo"
        size_hint: 1, None
        height: dp(130)
        mipmap: True
    ScrollView
        GridLayout
            cols: 1
            size_hint_y: None
            height: self.minimum_height
            MenuButton
                id: bt_sched
                text: 'Schedule'
                on_released: app.load_screen('ScreenSchedule', manager=app.navigation_manager)
            MenuButton
                text: 'Sponsors'
                on_released: app.load_screen('ScreenSponsor', manager=app.navigation_manager)
            MenuButton
                text: 'Venue'
                on_released: app.load_screen('ScreenVenue', manager=app.navigation_manager)
            MenuButton
                text: 'OpenSpaces'
                on_released: app.load_screen('ScreenOpenSpaces', manager=app.navigation_manager)
            MenuButton
                text: 'DevSprints'
                on_released: app.load_screen('ScreenDevSprints', manager=app.navigation_manager)
            MenuButton
                text: 'Feedback'
                on_released: app.load_screen('ScreenFeedback', manager=app.navigation_manager)
            MenuButton
                text: 'Ticket'
                on_released: app.load_screen('ScreenTicket', manager=app.navigation_manager)
            MenuButton
                text: 'Community'
                on_released: app.load_screen('ScreenCommunity', manager=app.navigation_manager)
            MenuButton
                text: 'About'
                on_released: app.load_screen('ScreenAbout', manager=app.navigation_manager)

<TopBar@BoxLayout>
    size_hint: None, None
    height: dp(45)
    width: dp(45)
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
    on_enter: 
        import os
        scr = os.environ.get('PYDELHI_STARTUP_SCREEN','ScreenSchedule')
        app.load_screen(scr, manager=app.navigation_manager)
    NavigationDrawer
        id: navigationdrawer
        on_parent: app.navigationdrawer = navigationdrawer
        LeftPanel
            id: left_panel
        RightPanel
            opacity: 1-(self.x/root.right)
''')
