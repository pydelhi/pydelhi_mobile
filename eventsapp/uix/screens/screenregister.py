from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
# from kivy.app import App


class ScreenFeedback(Screen):
    Builder.load_string('''
<ScreenRegister>
    name: 'ScreenRegiser'


''')

    def on_pre_enter(self):
        pass

    def on_enter(self):
        # read csv file here
        pass

    def register_attendee(self):
        pass

    def scan_qrcode(self):
        pass
