from kivy.network.urlrequest import UrlRequest


def on_success(*args, **kwargs):
    print "Successful! ", args

def on_failure(*args, **kwargs):
    print "Failure! ", args

def on_error(*args, **kwargs):
    print "Error! ", args


def get_data(endpoint):
    req = UrlRequest(
        'http://conference.pydelhi.org/api/' + endpoint + '.json',
        file_path='data/' + endpoint + '.json',
        on_success=on_success,
        on_error=on_error,
        on_failure=on_failure,
        timeout=2)

    import json

    jsondata = None

    with open('pydelhiconf/data/{}.json'.format(endpoint)) as fd:
        jsondata = json.load(fd)

    return jsondata