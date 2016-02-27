'''
PyDelhi App: 
- Displays Schedule: static
- Static map:
- Link to open location externally
- Talk/Workshop details
- Feedback
- Social Media:
	- Facebook
	- Twitter
'''

from datetime import datetime

from kivy.app import App
from kivy.clock import Clock
from kivy.properties import StringProperty


class PyDelhiApp(App):
    ''' Our main app class
    '''
    about_text = StringProperty('')

    time_left = StringProperty('')

    def build(self):
        self.about_text = '[b]About the conference[/b]\n\nPyDelhi Conference is an upcoming conference hosted by PyDelhi Community which focuses on using and developing using the Python programming language. The conference, now in its first year, will be conducted annually by the PyDelhi community. We hope to attract the best Python programmers from across the country and abroad. The main aim of the conference is to bring together startups and established companies, beginners and experts and plethora of global entrepreneurs under one roof. We will be inviting experts from various fields to showcase how Python is used by them and talk about new and upcoming technology.All the participants are expected to follow Code of Conduct\n\n\n[b]App Designed and implenented by PyDelhi Team visit us at [color=rgb(49,207,155)][ref=http://PyDelhi.org]http://PyDelhi.org[/ref][/color][/b]'
        self.icon = 'data/icon.png'

    def on_pause(self):
    	return True 

    def on_start(self):
        Clock.schedule_interval(self.calc_time_left, 1)

    def calc_time_left(self, dt):
        td = datetime(2016, 3, 5, 9) - datetime.now()
        days = td.days
        hours, remainder = divmod(td.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.time_left = '{}d, {}:{}:{} to go'.format(days, hours, minutes, seconds)

if __name__ == '__main__':
    PyDelhiApp().run()
