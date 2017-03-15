# -*- coding: utf8 -*-
'''App for PyDelhi Conf 2017:

Github Repo: http://github.com/
'''

__version__ = '0.0.3'



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
# from kivy.utils import platform
# from kivy.core.window import Window

# Kivy's properties are based on a observer pattern
# :ref: https://en.wikipedia.org/wiki/Observer_pattern
from kivy.properties import ListProperty, StringProperty, ObjectProperty

script_path = os.path.dirname(os.path.realpath(__file__))

# add module path for screen so they can be ynamically be imported
module_path = script_path + '/uix/screens/'
sys.path.insert(0, module_path)

# import webbrowser

# if platform == 'android':
#     from jnius import autoclass
#     from android.runnable import run_on_ui_thread

#     WebView = autoclass('android.webkit.WebView')
#     print "webview"
#     WebViewClient = autoclass('android.webkit.WebViewClient')
#     print "got client"
#     activity = autoclass('org.kivy.android.PythonActivity').mActivity
#     print "activity"

#     import os

#     @run_on_ui_thread
#     def initiate_webview():
#         webview = WebView(activity)
#         webbrowser._webview = webview
#         webbrowser._view_cached = activity.getCurrentFocus()
#         settings = webbrowser._webview.getSettings()
#         settings.setJavaScriptEnabled(True)
#         settings.setUseWideViewPort(True) # enables viewport html meta tags
#         settings.setLoadWithOverviewMode(True) # uses viewport
#         settings.setSupportZoom(True) # enables zoom
#         settings.setBuiltInZoomControls(True) # enables zoom controls
#         wvc = WebViewClient()
#         webbrowser._webview.setWebViewClient(wvc)
            
#     initiate_webview()

#     def _webopen(*args, **kwargs):
#         #print '9'*90
#         @run_on_ui_thread
#         def webopen(*args, **kwargs):
#             # open webview here
#             url = args[0]
#             print url, "<<<<<<<<<<<<<<<<<<"
#             webview = webbrowser._webview
#             webview.resumeTimers()
#             webview.clearHistory()
#             webview.loadUrl("about:blank")
#             webview.clearCache(True)
#             webview.freeMemory()
#             activity.setContentView(webview)
#             webbrowser._webview.loadUrl('{}'.format(url))
#             webbrowser._opened = True   

#         webopen(*args, **kwargs)
#         return True

#     @run_on_ui_thread
#     def close(*args):
#         if not webbrowser._webview:
#             print "no_webview"*20
#             return

#         wv = webbrowser._webview
#         wv.clearHistory()
#         wv.clearCache(True)
#         wv.loadUrl("about:blank")
#         print 'abt bank'*3
#         wv.freeMemory()
#         print 'free mem'*3
#         wv.pauseTimers()
#         print 'pause timers'*3
#         activity.setContentView(webbrowser._view_cached)
#         webbrowser._opened = False

#     webbrowser.open = _webopen
#     webbrowser.close = close


class PyConApp(App):
    ''' Our main app class:
    - 
    '''

    base_active_bright = ListProperty((226/255.,168/255.,180/255., 1))
    '''
    '''

    base_active_color = ListProperty([186/256., 106/256., 54./255, 1])
    '''This is the base Color in the app that is used to denote the currently
    active widgets, active buttons and highlited areas. Format
    is RGBA.

    :attr:`base_active_color` is a :class:`~kivy.properties.ListProperty`

    defaults to Red(217, 52, 47)
    '''

    base_inactive_color = ListProperty([141/256., 40/256., 40/256., 1])
    '''This is the base Color in the app that is used to denote the currently
    inactive items, inactive buttons and highlited areas. Format
    is RGBA.

    :attr:`base_inactive_color` is a :class:`~kivy.properties.ListProperty`

    defaults to Red(217, 52, 47)
    '''

    base_inactive_light = ListProperty([163/256., 112/256., 80/256., 1])
    '''This is the base Color in the app that is used to denote the currently
    active color used to display active buttons and highlited areas. Format
    is RGBA.

    :attr:`base_active_color` is a :class:`~kivy.properties.ListProperty`

    defaults to Red(225p, 224, 224)
    '''

    base_color = ListProperty([120./255, 64./255, 75./255, 1])
    '''This is the base Color in the app that is used to for bakgrounds.

    :attr:`base_color` is a :class:`~kivy.properties.ListProperty`

    defaults to Red(250, 250, 250, 1)
    '''

    event_name = StringProperty('')
    '''
    This is the name of the event.

    :attr:`event_name` is a :class:`~kivy.properties.StringProperty`

    defaults to ''
    '''

    venue_name = StringProperty('')
    '''
    This is the name of the venue.

    :attr:`venue_name` is a :class:`~kivy.properties.StringProperty`

    defaults to ''
    '''

    # def __init__(self):
    #     super(PyConApp, self).__init__()
    #     Window.bind(on_keyboard=self.on_back_button)

    def build(self):
        self.script_path = script_path
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
            screen_class = getattr(module, screen)
            sc = screen_class() 
            sc.from_back = not store_back
            setattr(self, module_path, sc)
            manager.add_widget(sc)

        else:
            sc = getattr(self, module_path)

        sc.from_back = not store_back
        manager.current = screen

        if store_back:
            self._navigation_higherarchy.append(sc)

        return getattr(self, module_path)

    # def on_back_button(self, window, key, *args):
    #     """ To be called whenever user presses Back/Esc Key """
    #     # If user presses Back/Esc Key
    #     if platform == 'android':
    #         if key == 27:
    #             import webbrowser
    #             print "here 0000000000"
    #             if hasattr(webbrowser, '_opened') and webbrowser._opened:
    #                 print "back press 999999999999999999999"
    #                 webbrowser.close()
    #                 return True
    #     else:
    #         pass


# Check if app is started as main and only then insitantiate the App class.
if __name__ == '__main__':
    PyConApp().run()
