'''ScreenSponsor:
Display all the information about venue.
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy_garden.mapview import MapView, MapMarker


class ScreenVenue(Screen):

    Builder.load_string('''
<ScreenVenue>
    name: 'ScreenVenue'
    directions: 'https://www.google.com/search?client=safari&rls=en&q=Conference+Centre%2C+University+of+Delhi&ie=UTF-8&oe=UTF-8#'
    url: 'https://www.du.ac.in/index.php?page=Conference-Centre'
    about: "Conference will be held in the Conference Centre on the University of Delhi.  This state of the art Conference Centre is located opposite the Department of Botany. This complex has a large air- conditioned conference hall, which can seat more than 300 people.\\nThe complex also has nine large and medium-sized committee rooms, board rooms, computer room, and space which can be used for video-conferencing and as a media centre. It has also a large room for coffee and tea breaks, a spacious and impressive lounge and a pantry. The Conference Centre has a beautiful green ambience. The University community organizes academic conferences, national and international, on campus in this Conference Centre.\\nThe Conference Centre is Accesible and Disabled friendly and passed the Access Audit conducted by the `National Centre for Accesible Environments` in 2008."
    venue_name: 'Conference Centre - Delhi University'
    streetview: ''
    gps: ["28.6877", "77.2103"]
    BoxLayout
        spacing: dp(13)
        orientation: 'vertical'
        padding: dp(4)
        BoxLayout
            orientation: 'vertical'
            SingleLineLabel:
                color: 0, 0, 0, 1
                text: app.venue_name
                halign: 'center'
                size_hint_y: None
                height: dp(25)
            AsyncImage:
                id: img_venue
                allow_stretch: True
                keep_ratio: True
        Splitter
            sizable_from: 'top'
            MapView:
                zoom: 11
                lat: float(root.gps[0])
                lon: float(root.gps[1])
                MapMarker
                    lat: float(root.gps[0])
                    lon: float(root.gps[1])
        BoxLayout:
            size_hint: 1, None
            height: dp(45)
            spacing: dp(13)
            padding: dp(4)
            Widget
                # this is a space holder
            ActiveButton:
                text: 'Open Street View'
                opacity: 1 if root.streetview else 0
                disabled: self.opacity == 0
                on_release:
                    import webbrowser
                    if root.streetview: webbrowser.open(root.street_view)
            ActiveButton:
                text: 'Get Directions'
                opacity: 1 if root.directions else 0
                on_release:
                    import webbrowser
                    if root.directions: webbrowser.open(root.directions)
''')

    def on_enter(self, onsuccess=False):
        from network import get_data
        event = get_data('event', onsuccess=onsuccess)
        if not event:
            return
        try:
            self.venue = event['0.0.1'][0]
        except KeyError:
            # no details for this talk exist...
            # let's go back to previous screen
            from utils import go_back_in_history
            go_back_in_history()
            return

        try:
            for item in 'directions', 'url', 'about', 'streetview', 'directions', 'gps':
                setattr(self, item, self.venue['venue_partners'][0][item])
        except (KeyError, IndexError) as err:
            print(err)
        self.venue_name = self.venue['venue_partners'][0]['name']
        self.ids.img_venue.source = self.venue['venue_partners'][0]['image']
