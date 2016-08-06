'''uix.pycon module which should house all common widgets.
'''

from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

class PyConScreenManager(ScreenManager):
	Builder.load_string('''
#:import WipeTransition kivy.uix.screenmanager.WipeTransition

<ImgBut@ButtonBehavior+Image>
    opacity: .5 if self.state =='down' else 1

<Background@Widget>
	source: ''
	color: 1, 1, 1, 1
	canvas.before:
    	Color:
    		rgba: root.color
    	Rectangle:
    		source: root.source
    		size: self.size
    		pos: self.pos

<PyConScreenManager>
	transition: WipeTransition()
''')