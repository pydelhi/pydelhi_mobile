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
    orientation: 'vertical'
    padding: dp(7), dp(7)
    Image
        source: "atlas://data/default/logo"
        size_hint: 1, None
        height: dp(130)
        mipmap: True
    Image
        id: img
        source: 'atlas://data/default/bg'
        allow_stretch: True
        color: app.base_active_color[:3] + [.5]
        keep_ratio: False
        ScrollView
            size: img.size
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
                # MenuButton
                #     text: 'DevSprints'
                #     on_released: app.load_screen('ScreenDevSprints', manager=app.navigation_manager)
                # MenuButton
                #     text: 'Feedback'
                #     on_released: app.load_screen('ScreenFeedback', manager=app.navigation_manager)
                MenuButton
                    text: 'Ticket'
                    on_released: app.load_screen('ScreenTicket', manager=app.navigation_manager)
                MenuButton
                    text: 'Community'
                    on_released: app.load_screen('ScreenCommunity', manager=app.navigation_manager)
                MenuButton
                    text: 'About'
                    on_released: app.load_screen('ScreenAbout', manager=app.navigation_manager)

<Topic@Label>
    opacity: 0
    canvas.before:
        Color
            rgba: 0, 0, 0, .5
        Rectangle
            texture: self.texture
            size: self.width - dp(50), self.height
            pos: self.x + dp(22), self.y - dp(2)
    font_size: dp(20)
    text_size: self.width - dp(50), self.height
    halign: 'left'
    valign: 'middle'

<TopBar@BoxLayout>
    size_hint: 1, None
    height: dp(45)
    canvas.before:
        Color:
            rgba: 92./256., 110./256., 118./255, 1
        Rectangle:
            size: self.size
            pos: self.pos
    ImBut
        color: 1, 1, 1, 1
        source: 'atlas://data/default/hamburger'
        size_hint_x: None
        size_hint_y: 1
        width: self.height
        allow_stretch: True
        on_released: app.navigationdrawer.toggle_state()

    Topic
        id: topic
        text: app.event_name


<RightPanel@BoxLayout+Background>
    source: 'atlas://data/default/bg'
    orientation: "vertical"
    TopBar
        id: topbar
    ScreenManager
        on_parent: app.navigation_manager = nav_sm
        id: nav_sm

<NavigationScreen>
    name: 'NavigationScreen'
    on_enter: 
        import os
        scr = os.environ.get('PYDELHI_STARTUP_SCREEN','ScreenSchedule')
        app.load_screen(scr, manager=app.navigation_manager)
        right_panel.ids.topbar.ids.topic.opacity=1
    NavigationDrawer
        id: navigationdrawer
        #anim_type: 'slide_above_anim'
        on_parent: app.navigationdrawer = navigationdrawer
        LeftPanel
            id: left_panel
        RightPanel
            id: right_panel
            opacity: 1-(self.x/root.right)
''')
