'''uix.pydelhiconf module which should house all common widgets.
'''

from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

class PyDelhiConfScreenManager(ScreenManager):
	Builder.load_string('''
#:import WipeTransition kivy.uix.screenmanager.WipeTransition

<ImgBut@ButtonBehavior+Image>
    color: 1, 1, 1, 1
    mipmap: True
    opacity: .5 if self.state =='down' else 1

<PyDelhiConfScreenManager>
	transition: WipeTransition()
''')