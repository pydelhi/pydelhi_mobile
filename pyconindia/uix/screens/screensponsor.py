'''ScreenSponsor:
Display all the logos of the sponsors.
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

class ScreenSponsor(Screen):

    
    Builder.load_string('''
<ScreenSponsor>
    name: 'ScreenSponsor'
    BoxLayout
        padding: dp(12)
        orientation: 'vertical'
        spacing: dp(4)
        Image
            source: 'atlas://data/default/fossee'
            allow_stretch: True
            size_hint: 1, 1
        BoxLayout
            orientation: 'vertical'
            spacing: dp(12)
            Image
                allow_stretch: True
                source: 'atlas://data/default/delhivery'
            BoxLayout
                orientation: 'vertical'
                Widget
                Image
                    allow_stretch: True
                    source: 'atlas://data/default/analyticsvidya'
        Button
            text: 'Sponsor Us'
            default: True
            size_hint_y: None
            height: dp(40)
            on_release: webbrowser.open('https://in.pycon.org/2016/sponsorship-prospectus.pdf')
        Button
            text: 'Contact Us'
            size_hint_y: None
            height: dp(40)
            on_release: webbrowser.open('mailto:sponsorship@in.pycon.org')
''')