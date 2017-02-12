# -*- coding: utf8 -*-
'''App for PyDelhi Conf 2017:

Github Repo: http://github.com/
'''

__version__ = '0.0.2'



# imports 
import os, sys
from os.path import abspath, dirname

# This allows you to use a custom data dir for kivy allowing you to
# load only the images that you set here in this dir.
# This way you avoid first loading kivy default images and .kv then
# loading your data files on top.
os.environ['KIVY_DATA_DIR'] = abspath(dirname(__file__)) + '/data'

# import App this is the main Class that manages UI's event loop
from kivy.app import App

# Kivy's properties are based on a observer pattern
# :ref: https://en.wikipedia.org/wiki/Observer_pattern
from kivy.properties import ListProperty, StringProperty, ObjectProperty

script_path = os.path.dirname(os.path.realpath(__file__))

# add module path for screen so they can be ynamically be imported
module_path = script_path + '/uix/screens/'
sys.path.insert(0, module_path)


class PyConApp(App):
    ''' Our main app class:
    - 
    '''

    base_active_color = ListProperty([85./255, 172./255, 238./255, 1])
    '''This is the base Color in the app that is used to denote the currently
    active widgets, active buttons and highlited areas. Format
    is RGBA.

    :attr:`base_active_color` is a :class:`~kivy.properties.ListProperty`

    defaults to Red(217, 52, 47)
    '''

    base_inactive_color = ListProperty([61/256., 61/256., 61/256., 1])
    '''This is the base Color in the app that is used to denote the currently
    inactive items, inactive buttons and highlited areas. Format
    is RGBA.

    :attr:`base_inactive_color` is a :class:`~kivy.properties.ListProperty`

    defaults to Red(217, 52, 47)
    '''

    base_inactive_light = ListProperty([225/256., 224/256., 224/256., 1])
    '''This is the base Color in the app that is used to denote the currently
    active color used to display active buttons and highlited areas. Format
    is RGBA.

    :attr:`base_active_color` is a :class:`~kivy.properties.ListProperty`

    defaults to Red(225p, 224, 224)
    '''

    base_color = ListProperty([250/256., 250/256., 250/256., 1])
    '''This is the base Color in the app that is used to for bakgrounds.

    :attr:`base_color` is a :class:`~kivy.properties.ListProperty`

    defaults to Red(250, 250, 250, 1)
    '''

    def build(self):
        self.icon = 'data/icon.png'
        # Here we build our own navigation higherarchy.
        # So we can decide what to do when the back
        # button is pressed.
        self._navigation_higherarchy = []
        # this is the main entry point of our app
        from uix.pydelhiconf import PyDelhiConfScreenManager
        sm = PyDelhiConfScreenManager()
        # This `sm` is the root widget of our app refered by app.root
        return sm

    def on_pause(self):
        # return True to allow for the app to pause
        return True 

    def on_start(self):
        # bind to the keyboard to listen to 
        # specific key codes
        from utils.keyboard import hook_keyboard
        hook_keyboard()
        # let's load our first screen
        self.load_screen('StartupScreen')


    def go_back_in_history(self):
        try:
            scr = self._navigation_higherarchy.pop()
            if scr.name == 'ScreenSchedule':
                from utils import pause_app
                pause_app()
                return
            scr = self._navigation_higherarchy[-1]
            self.load_screen(
                scr.name,
                manager=scr.manager,
                store_back=False)
        except IndexError: 
            # at root of app. Pause it.
            from utils import pause_app
            pause_app()

    def load_screen(self, screen, manager=None, store_back=True):
        '''Load the provided screen:
        arguments::
            `screen`: is the name of the screen to be loaded
            `manager`: the manager to load this screen, this defaults to
            the main class.
        '''
        store_back = False if screen == 'StartupScreen' else store_back

        manager = manager or self.root
        # load screen modules dynamically
        # for example load_screen('LoginScreen')
        # will look for uix/screens/loginscreen
        # load LoginScreen 
        module_path = screen.lower()
        if not hasattr(self, module_path):
            import imp
            module = imp.load_module(screen, *imp.find_module(module_path))
            print "module ", module
            screen_class = getattr(module, screen)
            print "screen_class ", screen_class
            sc = screen_class()
            setattr(self, module_path, sc)
            manager.add_widget(sc)

        else:
            sc = getattr(self, module_path)
        manager.current = screen

        if store_back:
            self._navigation_higherarchy.append(sc)

        return getattr(self, module_path)


# Check if app is started as main and only then insitantiate the App class.
if __name__ == '__main__':
    PyConApp().run()
