'''A simple App made for managing and attending events.
'''

from kivy.app import App


class EventsApp(App):
    '''This is our entry point for the application
    '''
    
    def load_screen(self):
        '''Load screens dynamically
        '''

    def on_pause(self):
        # allow the app to pause on android and ios
        return True

    def on_resume(self):
        pass



if __name__ == '__main__':
    EventsApp().run()
