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
from kivy.properties import StringProperty, ObjectProperty
from kivy.factory import Factory

Factory.register('TouchRippleBehavior', module='uix.behaviors')
Factory.register('TabbedCarousel', module='uix.tabbedcarousel')

class PyDelhiApp(App):
    ''' Our main app class
    '''
    about_text = StringProperty('')

    time_left = StringProperty('')

    def build(self):
        self.about_text = '[b]About the conference[/b]\n\nPyDelhi conference is hosted annually by Pydelhi community with an aim to promote Python programming language. We provide a single platform to users from different spheres such as students, global entrepreneur and professionals from startup and established firms to connect and share their ideas. Experts from various domains showcase their use of Python besides discussing about the recent and upcoming trends in technology.\n\n\n[b]App designed and implenented by PyDelhi Team visit us at [color=rgb(49,207,155)][ref=http://PyDelhi.org]http://PyDelhi.org[/ref][/color][/b]'
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
