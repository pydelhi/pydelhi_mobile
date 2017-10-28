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
            title: 'Shaheed Sukhdev College of Business Studies'
        BoxLayout:
            MapView:
                zoom: 12
                lat: 28.7312221
                lon: 77.1203375
                MapMarker
                    lat: 28.7312221
                    lon: 77.1203375
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
                    webbrowser.open('https://www.google.co.in/maps/dir/''/Shaheed+Sukhdev+College+Of+Business+Studies')

''')
