from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.app import App
import webbrowser


class ScreenFeedback(Screen):
    Builder.load_string('''
<ScreenFeedback>
    name: 'ScreenFeedback'
''')
    def on_enter(self):
        webbrowser.open('http://pydelhi.vkd.me/')
        app = App.get_running_app()
        app.go_back_in_history()