'''ScreenSponsor:
Display all the information about venue.
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.garden.mapview import MapView

class ScreenVenue(Screen):
    
    Builder.load_string('''
<ScreenVenue>
    name: 'ScreenVenue'
    BoxLayout
        spacing: dp(13)
        orientation: 'vertical'
        padding: dp(4)
        Image:
            source: 'atlas://data/default/venue'
            allow_stretch: True
            keep_ratio: True
        Label:
            text: 'IIM Lucknow, Noida campus'
            size_hint: 1, None
            padding: dp(4), dp(4)
            color: 0, 0, 1, 1
        BoxLayout:
            BoxLayout:
                spacing: dp(13)
                orientation: 'vertical'
                padding: dp(4)
                Image:
                    source: 'atlas://data/default/venueinfo'
                    allow_stretch: True
                    keep_ratio: True
            BoxLayout:
                spacing: dp(13)
                orientation: 'vertical'
                padding: dp(4)
                Button:
                    size_hint: 1, None
                    height: dp(72)
                    background_color: 1, 0, 0, 1
                    color: 1, 1, 1, 1
                    opacity: .5 if self.state == 'down' else 1
                    text: 'Open Street View'
                    
                    # MapView:
                    #     zoom: 11
                    #     lat: 50.6394
                    #     lon: 3.057 
                Button:
                    size_hint: 1, None
                    height: dp(72)
                    background_color: 1, 0, 0, 1
                    color: 1, 1, 1, 1
                    opacity: .5 if self.state == 'down' else 1
                    text: 'Get Directions'
                    on_release:
                        # import webbrowser
                        # webbrowser.open('https://www.google.co.in/maps/dir/''/iim+lucknow+noida+campus') 
''')