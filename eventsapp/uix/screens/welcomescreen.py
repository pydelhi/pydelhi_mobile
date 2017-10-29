'''
Welcome Screen
==============
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.app import App


class WelcomeScreen(Screen):

    Builder.load_string('''
<WelcomeScreen>
    name: 'WelcomeScreen'
    BoxLayout
        orientation: 'vertical'
        TopBar
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
                    text: 'Welcome to\\n PyCon India 2017'
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
                    Button
                        size_hint: 1, .1
                        font_size: dp(18)
                        text: 'Workshop & DevSprints'
                        background_normal: 'data/images/btn.png'
                        background_down: 'data/images/btn.png'
                        opacity: .8 if self.state == 'normal' else .6
                        on_release: root.on_press_schedule('workshop')
                    Button
                        size_hint: 1, .1
                        font_size: dp(18)
                        text: 'Conference Days'
                        background_normal: 'data/images/btn.png'
                        background_down: 'data/images/btn.png'
                        opacity: .8 if self.state == 'normal' else .6
                        on_release: root.on_press_schedule('conference')
    ''')

    def on_press_schedule(self, scheduletype):
        app = App.get_running_app()
        app.scheduledatatype = scheduletype
        manager = app.navigation_screen.ids.nav_manager
        app.load_screen('ScheduleScreen', manager=manager)
