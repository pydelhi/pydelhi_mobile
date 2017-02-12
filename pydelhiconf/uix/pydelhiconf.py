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

<Background@Widget>
	source: ''
	color: app.base_color
	canvas.before:
    	Color:
    		rgba: root.color if root.color else (1, 1, 1, 1)
    	Rectangle:
    		source: root.source
    		size: self.size
    		pos: self.pos

<PyDelhiConfScreenManager>
	transition: WipeTransition()
''')