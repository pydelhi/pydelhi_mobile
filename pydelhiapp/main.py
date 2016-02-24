'''
'''


from kivy.app import App
from kivy.properties import StringProperty

class PyDelhiApp(App):

	about_text = StringProperty('')

	def on_start(self):
		self.about_text = '''
**About the conference**\n\n
PyDelhi Conference is an upcoming conference 
hosted by PyDelhi Community which focuses on 
using and developing using the Python programming 
language. The conference, now in its first year, 
will be conducted annually by the PyDelhi community. 
We hope to attract the best Python programmers from 
across the country and abroad. The main aim of the 
conference is to bring together startups and established 
companies, beginners and experts and plethora of global 
entrepreneurs under one roof. We will be inviting experts 
from various fields to showcase how Python is used by them 
and talk about new and upcoming technology.All the participants 
are expected to follow Code of Conduct'''

if __name__ == '__main__':
    PyDelhiApp().run()
