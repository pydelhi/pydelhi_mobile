'''ScreenHistory
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


class ScreenHistory(Screen):
    Builder.load_string('''
<ScreenHistory>
    name: 'ScreenHistory'
''')

    def on_enter(self):
        pass
