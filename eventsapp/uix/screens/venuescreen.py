'''
Venue Screen
==============
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.garden.mapview import MapView
from kivy.garden.mapview import MapMarker


class VenueScreen(Screen):

    Builder.load_string('''
<VenueScreen>
    name: 'VenueScreen'
    BoxLayout
        orientation: 'vertical'
        canvas:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                size: self.size
                pos: self.pos
        TopBar:
            title: 'Hyderabad International Convention Centre'
        BoxLayout:
            MapView:
                zoom: 12
                lat: 17.4728898
                lon: 78.3733243
                MapMarker
                    lat: 17.4728898
                    lon: 78.3733243
        BoxLayout:
            padding: dp(10), dp(10)
            size_hint: 1, .1
            Button:
                text: 'Get Directions'
                font_size: dp(22)
                background_normal: 'data/images/btn.png'
                background_down: 'data/images/btn.png'
                opacity: 1 if self.state == 'normal' else .9
                on_release:
                    import webbrowser
                    webbrowser.open('https://www.google.co.in/maps/dir/''/17.4728898,78.3733243/@17.47289,78.373324,14z?hl=en-IN')

''')
