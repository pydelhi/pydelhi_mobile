from kivy.network.urlrequest import UrlRequest
from kivy.app import App
app = App.get_running_app()
import os

def on_success(req, oldata, endpoint):
    # got new data, update the schedule
    ndata = None
    with open(req.file_path) as f:
        ndata = f.read()
    if ndata == oldata:
        return
    # check which endpoint got a response
    app.screenschedule.on_enter(onsuccess=True)

def on_failure(*args, **kwargs):
    print "Failure! ", args

def on_error(*args, **kwargs):
    print "Error! ", args


def get_data(endpoint, onsuccess=False):
    filepath = app.script_path + '/data/' + endpoint + '.json'
    
    #use od data to check if anything in the data has been updated.
    oldata = None
    with open(filepath) as f:
        oldata = f.read()

    if os.environ.get("PYDELHI_OFFLINE_MODE", None) == '1':
        onsuccess = True
    if not onsuccess:
        req = UrlRequest(
            'http://conference.pydelhi.org/api/' + endpoint + '.json',
            file_path=filepath,
            on_success=lambda req ,r2:on_success(req, oldata, endpoint),
            on_error=on_error,
            on_failure=on_failure,
            timeout=2)
        print vars(req)
    import json
    
    jsondata = {}

    try:
        with open(filepath) as fd:
            jsondata = json.load(fd)
    except (IOError, ValueError) as err:
        import time
        # give thread a chance to download and fix data
        time.sleep(2)

    return jsondata
