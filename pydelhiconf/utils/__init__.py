__all__ = ['keyboard', 'pause_app']

from kivy.app import App

def pause_app():
    '''
    '''
    from kivy.utils import platform
    if platform == 'android':
        from jnius import cast
        from jnius import autoclass
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
        currentActivity.moveTaskToBack(True)
    else:
        app = App.get_running_app()
        app.stop()