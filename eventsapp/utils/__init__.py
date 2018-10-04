__all__ = ['keyboard', 'pause_app']

from kivy.app import App
from kivy.utils import platform
from kivy.uix.screenmanager import ScreenManagerException

if platform == 'android':
    from jnius import autoclass, cast
    JS = autoclass('java.lang.String')
    Intent = autoclass('android.content.Intent')
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    currentActivity = cast('android.app.Activity', PythonActivity.mActivity)


def pause_app():
    '''
    '''
    if platform == 'android':
        currentActivity = cast(
            'android.app.Activity', PythonActivity.mActivity)
        currentActivity.moveTaskToBack(True)
    else:
        app = App.get_running_app()
        app.stop()


def set_reminder(self, title, time):
    intent = Intent()
    Calendar = autoclass('java.util.Calendar')
    calendar = Calendar.getInstance()
    calendar.setTimeInMillis(1480103863835)
    intent.setType("vnd.android.cursor.item/event")
    intent.putExtra(Events.DESCRIPTION, "Download Examples")
    intent.putExtra("title", "A Test Event from android app");
    intent.setAction(Intent.ACTION_VIEW)
    PythonActivity.mActivity.startActivity(intent)


def do_share(data, title):
    if platform != 'android':
        return
    sendIntent = Intent()
    sendIntent.setAction(Intent.ACTION_SEND)
    sendIntent.setType("text/plain")
    sendIntent.putExtra(Intent.EXTRA_TEXT, JS(data))
    it = Intent.createChooser(
        sendIntent, cast('java.lang.CharSequence', JS(title)))
    currentActivity.startActivity(it)


def scan_qr(on_complete):
    if platform != 'android':
        return
    from jnius import autoclass
    from android import activity
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    SimpleScannerActivity = autoclass(
        "org.pythonindia.qr.SimpleScannerActivity")
    Intent = autoclass('android.content.Intent')
    intent = Intent(PythonActivity.mActivity, SimpleScannerActivity)

    def on_qr_result(requestCode, resultCode, intent):
        try:
            if resultCode == -1:  # RESULT_OK:
                #  this doesn't work due to some bug in jnius:
                # contents = intent.getStringExtra("text")
                String = autoclass("java.lang.String")
                contents = intent.getStringExtra(String("text"))
                on_complete(contents)
        finally:
            activity.unbind(on_activity_result=on_qr_result)
    activity.bind(on_activity_result=on_qr_result)
    PythonActivity.mActivity.startActivityForResult(intent, 0)


def load_screen(screen, manager=None, store_back=True):
    '''Load the provided screen:
    arguments::
        `screen`: is the name of the screen to be loaded
        `manager`: the manager to load this screen, this defaults to
        the main class.
    '''
    app = App.get_running_app()
    store_back = False if screen == 'StartupScreen' else store_back

    manager = manager or app.root
    # load screen modules dynamically
    # for example load_screen('LoginScreen')
    # will look for uix/screens/loginscreen
    # load LoginScreen
    module_path = screen.lower()
    if not hasattr(app, module_path):
        import imp
        module = imp.load_module(screen, *imp.find_module(module_path))
        screen_class = getattr(module, screen)
        sc = screen_class()
        sc.from_back = not store_back
        setattr(app, module_path, sc)
        manager.add_widget(sc)

    else:
        sc = getattr(app, module_path)

    sc.from_back = not store_back
    manager.current = screen

    if store_back:
        app._navigation_higherarchy.append(sc)

    return getattr(app, module_path)


def go_back_in_history():
    app = App.get_running_app()
    from utils import pause_app
    try:
        scr = app._navigation_higherarchy.pop()
        if scr.name == 'ScreenSchedule':
            # we are at top of Nav higherarchy
            pause_app()
            return

        # we are not at root of Nav higherarchy
        scr = app._navigation_higherarchy[-1]
        load_screen(
            scr.name,
            manager=scr.manager,
            store_back=False)
    except IndexError, ScreenManagerException:
        # check if current screen is schedule screen?
        if app.navigation_manager.current == 'ScreenSchedule':
            pause_app()
