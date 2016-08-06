__all__ = ['keyboard', 'pause_app']

from kivy.app import App
import threading
import pickle 

app = App.get_running_app()

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
        app.stop()


def fetch_data():
    '''
    - Download data using junction client.
    - on_success: Store data in local database

    Cause Junction Client is blocking, we have to
    call it using a thread that does not  block the UI.
    For this purpose we will start the thread using
    target _fetch_data.
    '''
    threading.Thread(target=_fetch_data).start()

# def _fetch_data(conference='2016'):
#     conf = {
#         '2016': 0,
#         '2015': 1,
#         '2014': 2,
#         '2013': 3}
#     from junction import JunctionClient
    
#     pconf = None
#     path = './junctionclient.pkl'
#     try:
#         # fetch data
#         client = JunctionClient('https://in.pycon.org/cfp/')
#         from pudb import set_trace; set_trace()
#         # save_data
#         pconf = client.conferences[conf[conference]]

#         with open(path, 'wb') as fl:
#             pickle.dump(pconf, fl, pickle.HIGHEST_PROTOCOL)
#     except Exception as e:
#         print(e)
#     # read data from disk
#     with open(path) as fl:
#         pconf = pickle.load(fl)

#     print pconf.schedule
    
#     if not app.conference:
#         app.conference = pconf
#         return

#     # compare and update app.client only if something has changed
#     if pickle.dumps(app.conference, pickle.HIGHEST_PROTOCOL) != pickle.dumps(conference, pickle.HIGHEST_PROTOCOL):
#         print('conference data updated')
#         app.conference = pconf 

