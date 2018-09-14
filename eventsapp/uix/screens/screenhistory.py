'''ScreenHistory
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.app import App


class ScreenHistory(Screen):
    Builder.load_string('''
<ScreenHistory>
    name: 'ScreenHistory'
''')

    def on_enter(self):
        app = App.get_running_app()
        app.go_back_in_history()
