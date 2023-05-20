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
    directions: ''
    url: 'https://google.com'
    about: 'About Venue here'
    venue_name: ''
    streetview: ''
    directions: "https://www.google.com/maps/dir//Indian+Institute+of+Technology+Delhi,+IIT+Delhi+Main+Rd,+IIT+Campus,+Hauz+Khas,+New+Delhi,+Delhi+110016/data=!4m7!4m6!1m1!4e2!1m2!1m1!1s0x390d1df6b9055fb5:0x81c10b266b1ea3c0!3e0?sa=X&ved=2ahUKEwjeqdGbwoP_AhUQPewKHROvCdAQox16BAgcEBQ"
    gps: ["28.5457", "77.1928"]
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
