'''ScreenSponsor:
Display all the logos of the sponsors.
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from network import get_data
from kivy.factory import Factory
from kivy.uix.stacklayout import StackLayout



class Sponsor(StackLayout):
    data = ObjectProperty(None)


class ScreenSponsor(Screen):

    
    Builder.load_string('''
<ScreenSponsor>
    name: 'ScreenSponsor'
    BoxLayout
        orientation: 'vertical'
        spacing: dp(4)
        id:main
        BackLabel
            text: "Sponsors"
            backcolor: app.base_inactive_color[:3] + [.5]
            pos_hint:{'top':1}
            size_hint: 1 , None
            height: dp(10)
            font_size:dp(20)
        
<Footer@BoxLayout>
    size_hint_y: .2
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

<Sponsor@StackLayout>
    orientation: 'tb-rl'
    spacing: dp(12)
    size_hint: 1, 1
    BackLabel
        text: self.parent.data['name']
        size_hint: 1, None
        height: dp(17)
        font_size:dp(15)
    
    SponsorImage


<SponsorImage@ButtonBehavior+AsyncImage>
    size_hint:1,.8
    halign: 'center'
    padding: dp(10), dp(10)
    valign: 'middle'
    allow_stretch:False
    source: self.parent.data['logo']
    on_release:
        import webbrowser
        webbrowser.open(self.parent.data['website'])
    

''')

    def on_enter(self, onsuccess=False):
        '''Series of actions to be performed when Schedule screen is entered
        '''

        # this should update the file on disk
        sponsors = get_data('sponsors', onsuccess=onsuccess).get('0.0.1')
        main_box = self.ids.main;
        main_box.clear_widgets()
        for s in sponsors:
            bl = Factory.Sponsor(size_hint_y=.8/len(sponsors), data=s)
            main_box.add_widget(bl)
        footer = Factory.Footer()
        main_box.add_widget(footer)

# Label
#         Text:getattr(self, 'data',{}).get('logo')
#     Label
#         Text:getattr(self, 'data',{}).get('logo')
