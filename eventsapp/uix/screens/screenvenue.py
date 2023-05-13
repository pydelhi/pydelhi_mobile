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
                source: 'https://geospatialworldforum.org/2018/images/HICC.jpg'
                allow_stretch: True
                keep_ratio: True
        Splitter
            sizable_from: 'top'
            MapView:
                zoom: 11
                lat: 17.4728898
                lon: 78.3733243
                MapMarker
                    lat: 17.4728898
                    lon: 78.3733243
        BoxLayout:
            size_hint: 1, None
            height: dp(45)
            spacing: dp(13)
            padding: dp(4)
            Widget
                # this is a space holder
            # ActiveButton:
            #     text: 'Open Street View'
            ActiveButton:
                text: 'Get Directions'
                on_release:
                    import webbrowser
                    webbrowser.open("https://www.google.com/maps/dir//hyderabad+international+convention+center/data=!4m6!4m5!1m1!4e2!1m2!1m1!1s0x3bcb922df075a857:0x4ee11f87406cbdf1?sa=X&ved=2ahUKEwi796TB_7fdAhUThbwKHeBuCLgQ9RcwAHoECAEQCQ") 
''')

