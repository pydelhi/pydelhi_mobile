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
             |___ screens: "This is where all our UI screens of the app go."
|
|___ tools: "This is where all our tools including assets etc go."
       |___ images: "This is where all our image assets go'
       |___ raw_assets: "This is where the raw assets from the design team go"
|___ tests: "All our tests go here"
'''

# imports 
import os, sys
from os.path import abspath, dirname
script_path = os.path.dirname(os.path.realpath(__file__))

# add module path for screen so they can be dynamically be imported
module_path = script_path + '/uix/screens/'
sys.path.insert(0, module_path)


from kivy.app import App


class EventsApp(App):
    '''This is our entry point for the application
    '''
    
    def build(self):
       from kivy.uix.screenmanager import ScreenManager
       root = ScreenManager()
       #return the root widget here
       return root

    def on_start(self):
       self.load_screen('LogoScreen')
    
    def on_pause(self):
        # allow the app to pause on android and ios
        return True

    def on_resume(self):
        pass

    def load_screen(self, screen, manager=None, store_back=True):
        '''Load the provided screen:
        arguments::
            `screen`: is the name of the screen to be loaded
            `manager`: the manager to load this screen, this defaults to
            the root screen manager.
        '''
        # store_back is used to load the previous screen when a user
        # chooses to press back, the last screen in the navigation
        # higherarchy is loaded
        store_back = False if screen == 'StartupScreen' else store_back

        # Default manager is the root widget.
        # override that with the manager argument if passed.
        manager = manager or self.root
        # load screen modules dynamically
        # for example load_screen('LoginScreen')
        # will look for uix/screens/loginscreen
        # load LoginScreen 
        module_path = screen.lower()
        if not hasattr(self, module_path):
            import imp
            module = imp.load_module(screen, *imp.find_module(module_path))
            screen_class = getattr(module, screen)
            sc = screen_class() 
            sc.from_back = not store_back
            setattr(self, module_path, sc)
            manager.add_widget(sc)

        else:
            sc = getattr(self, module_path)

        sc.from_back = not store_back
        manager.current = screen

        # if store_back:
        #     self._navigation_higherarchy.append(sc)

        return getattr(self, module_path)


# is our app being launched by python interpretter directly?
# or is it being imported as a module?
if __name__ == '__main__':
    # app is being run directly
    # instanciate our app and run it.
    EventsApp().run()
