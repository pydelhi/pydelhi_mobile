'''uix.pyconf module which should house all common widgets.
'''

from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder


class PyConfScreenManager(ScreenManager):
    Builder.load_string('''
#:import WipeTransition kivy.uix.screenmanager.WipeTransition

<PyConfScreenManager>
    transition: WipeTransition()
''')
