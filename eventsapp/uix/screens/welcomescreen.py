'''
Welcome Screen
==============
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.app import App
from uix.buttons import ThemeButton


class WelcomeScreen(Screen):

    Builder.load_string('''
<WelcomeScreen>
    name: 'WelcomeScreen'
    BoxLayout
        orientation: 'vertical'
        TopBar
            title: 'PyCon India 2018'
        RelativeLayout
            Image
                source: 'data/images/navback.png'
                allow_stretch: True
                keep_ratio: False
            Image
                source: 'data/images/overlay.png'
                allow_stretch: True
                keep_ratio: False
            BoxLayout
                orientation: 'vertical'
                Label
                    text: 'Welcome to\\n PyCon India 2018'
                    text_size: self.size
                    valign: 'center'
                    halign: 'center'
                    font_size: dp(34)
                    color: 1, 1, 1, 1
                    bold: True
                BoxLayout
                    orientation: 'vertical'
                    spacing: dp(45)
                    padding: dp(45), dp(45)
                    ThemeButton:
                        size_hint: 1, .1
                        text: 'Workshop & DevSprints'
                        on_release: root.on_press_schedule('workshop')
                    ThemeButton:
                        size_hint: 1, .1
                        text: 'Conference Days'
                        on_release: root.on_press_schedule('conference')
    ''')

    def on_press_schedule(self, scheduletype):
        app = App.get_running_app()
        app.scheduledatatype = scheduletype
        manager = app.navigation_screen.ids.nav_manager
        app.load_screen('ScheduleScreen', manager=manager)
