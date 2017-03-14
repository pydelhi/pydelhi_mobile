'''ScreenSponsor:
Display all the information about venue.
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.garden.mapview import MapView
from kivy.garden.mapview import MapMarker

class ScreenVenue(Screen):
    
    Builder.load_string('''
<ScreenVenue>
    name: 'ScreenVenue'
    BoxLayout
        spacing: dp(13)
        orientation: 'vertical'
        padding: dp(4)
        BoxLayout
            orientation: 'vertical'
            SingleLineLabel:
                text: app.venue_name
                halign: 'center'
                size_hint_y: None
                height: dp(25)
            AsyncImage:
                id: img_venue
                source: 'atlas://data/default/venue'
                allow_stretch: True
                keep_ratio: True
        Splitter
            sizable_from: 'top'
            MapView:
                zoom: 11
                lat: 28.6235184
                lon: 77.3551479 
                MapMarker
                    lat: 28.6235184
                    lon: 77.3551479
        BoxLayout:
            size_hint: 1, None
            height: dp(45)
            spacing: dp(13)
            padding: dp(4)
            ActiveButton:
                text: 'Open Street View'
            ActiveButton:
                text: 'Get Directions'
                on_release:
                    import webbrowser
                    webbrowser.open('https://www.google.co.in/maps/dir/''/iim+lucknow+noida+campus') 
''')

