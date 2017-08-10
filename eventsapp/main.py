'''A simple App made for managing and attending events.

Step 1 setting up the basic structure of the app

PyCon-Mobile-App
|
|___ LICENSE
|___ Makefile
|___ README.md
|___ eventsapp
       |___ main.py: "This is the main entry point of our application"
       |___ uix: "This is where our user interface elements go."
             |___ 
|
|___ tools: "This is where all our tools including assets etc go."
       |___ images: 'this is where all our image assets go'
|___ tests: "All our tests go here"
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
