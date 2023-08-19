'''Keyboard utils
'''
from kivy.app import App

def hook_keyboard(*args):
    from kivy.base import EventLoop
    EventLoop.window.bind(on_keyboard=_hook_keyboard)


def _hook_keyboard(window, key, *largs):
    app = App.get_running_app()
    if key == 27:
        # do what you want,
        # return True for stopping the propagation to widgets.
        # indicating we consumed the event.
        app.go_back_in_history()
        return True
