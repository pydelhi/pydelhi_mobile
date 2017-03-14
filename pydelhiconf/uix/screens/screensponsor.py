'''ScreenSponsor:
Display all the logos of the sponsors.
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from network import get_data
from kivy.properties import ObjectProperty
from kivy.factory import Factory
from kivy.uix.stacklayout import StackLayout
from kivy.uix.popup import Popup


class Sponsor(StackLayout):
    ''' This is a simple StackLayout that holds the image 
    '''
    data = ObjectProperty(None)


class ScreenSponsor(Screen):

    
    Builder.load_string('''
<ScreenSponsor>
    name: 'ScreenSponsor'
    BoxLayout
        orientation: 'vertical'
        spacing: dp(4)
        id:main
        
<Footer@BoxLayout>
    size_hint_y: .2
    padding: dp(9)
    spacing: dp(9)
    ActiveButton
        text: 'Sponsor Us'
        size_hint_y: None
        height: dp(40)
        on_release:
            import webbrowser
            webbrowser.open('https://in.pycon.org/2016/sponsorship-prospectus.pdf')
    ActiveButton
        text: 'Contact Us'
        size_hint_y: None
        height: dp(40)
        on_release:
            import webbrowser
            webbrowser.open('mailto:sponsorship@in.pycon.org')

<Sponsor>
    orientation: 'tb-rl'
    spacing: dp(12)
    size_hint: 1, 1
    Label
        text: self.parent.data['name']
        size_hint: 1, None
        height: dp(20)
        font_size:dp(18)
    SponsorImage
        on_release:
            import webbrowser
            webbrowser.open(root.data['website'])

<SponsorImage@ButtonBehavior+AsyncImage>
    size_hint:1,.8
    halign: 'center'
    padding: dp(10), dp(10)
    valign: 'middle'
    allow_stretch:False
    source: self.parent.data['logo']

''')

    def on_enter(self, onsuccess=False):
        '''Series of actions to be performed when Schedule screen is entered
        '''

        # this should update the file on disk
        sponsors = get_data('sponsors', onsuccess=onsuccess)
        if not sponsors:
            return

        sponsors = sponsors.get('0.0.1')
        main_box = self.ids.main;
        main_box.clear_widgets()
        for s in sponsors:
            bl = Factory.Sponsor(size_hint_y=.8/len(sponsors), data=s)
            main_box.add_widget(bl)
        footer = Factory.Footer()
        main_box.add_widget(footer)

