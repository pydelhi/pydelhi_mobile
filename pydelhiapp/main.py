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

#from background_services import update_from_remote_schedule

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
    #     Clock.schedule_interval(self.calc_time_left, 1)
        #self.load_local_schedule()
        #update_from_remote_schedule(callback=schedule_callback)
        pass

    def schedule_callback(self, status, data):
        if status == 'success':
            # update schedule
            self.load_data(data)

    def load_local_schedule(self):
        import json
        data = json.load(open('data/pydelhi-conf-events.json'))
        self.load_data(data)

    def load_data(self, data):
        grid = self.root.ids.grid_audi_3
        grid.clear_widgets()
        EventItem = Factory.EventItem
        gridadd = grid.add_widgets
        for hall in data.keys():
            talks = data[hall]
            for talk in talks:
                title = talk['schedule-item-date']
                date = talk['schedule-item-date']
                text = talk['schedule-item-text']
                gridadd(EventItem(title=title, time=date, spkrdetail=text))


    # def calc_time_left(self, dt):
    #     td = datetime(2016, 3, 5, 9) - datetime.now()
    #     days = td.days
    #     hours, remainder = divmod(td.seconds, 3600)
    #     minutes, seconds = divmod(remainder, 60)
    #     self.time_left = '{}d, {}:{}:{} to go'.format(days, hours, minutes, seconds)

if __name__ == '__main__':
    PyDelhiApp().run()
