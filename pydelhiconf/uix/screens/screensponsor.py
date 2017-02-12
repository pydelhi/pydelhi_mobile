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
        AsyncImage
            source: 'https://conference.pydelhi.org/img/platinum_sponsor.jpg'
            allow_stretch: True
            size_hint: 1, 1
        BoxLayout
            orientation: 'vertical'
            spacing: dp(12)
            Image
                allow_stretch: True
                source: ''
            BoxLayout
                orientation: 'vertical'
                Widget
                Image
                    allow_stretch: True
                    source: ''
        BoxLayout
            size_hint_y: None
            height: dp(50)
            PyConButton
                text: 'Sponsor Us'
                default: True
                size_hint_y: None
                height: dp(40)
                on_release:
                    import webbrowser
                    webbrowser.open('https://in.pycon.org/2016/sponsorship-prospectus.pdf')
            PyConButton
                text: 'Contact Us'
                size_hint_y: None
                height: dp(40)
                on_release:
                    import webbrowser
                    webbrowser.open('mailto:sponsorship@in.pycon.org')
''')