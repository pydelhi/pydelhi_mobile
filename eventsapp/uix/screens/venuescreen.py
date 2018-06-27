'''
Venue Screen
==============
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
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
            title: 'Hyderabad International Convention Centre (HICC)'
        BoxLayout:
            MapView:
                zoom: 12
                lat: 17.47289
                lon: 78.373324
                MapMarker
                    lat: 17.47289
                    lon: 78.373324
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
                    webbrowser.open('https://www.google.com/maps?ll=17.47289,78.373324&z=14&t=m&hl=en-GB&gl=IN&mapclient=embed&cid=5683858870480190961')

''')
