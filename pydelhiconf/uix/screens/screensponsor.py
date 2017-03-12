'''ScreenSponsor:
Display all the logos of the sponsors.
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from network import get_data
from kivy.properties import ObjectProperty
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout


class Sponsor(BoxLayout):
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
    id:footer
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

<Sponsor@BoxLayout>
    orientation: 'vertical'
    spacing: dp(12)
    size_hint: 1, 1
    
    Label
        text: self.parent.data['name']
        
    AsyncImage
        size_hint:.8,.8
        halign: 'center'
        valign: 'middle'
        allow_stretch:True
        source: self.parent.data['logo']
    
    Label
        text: self.parent.data['about']
        size_hint:1,None
        padding: dp(5), dp(10)
        font_size: dp(10)
        halign:'left'
        text_size: self.width, None
''')

    def on_enter(self, onsuccess=False):
        '''Series of actions to be performed when Schedule screen is entered
        '''

        # this should update the file on disk
        sponsors = get_data('sponsors', onsuccess=onsuccess).get('0.0.1')
        main_box = self.ids.main;

        for s in sponsors:
            bl = Factory.Sponsor(size_hint_y=1/len(sponsors), data=s)
            main_box.add_widget(bl)
        # footer = self.ids.footer;
        # main_box.add_widget(footer)

# Label
#         Text:getattr(self, 'data',{}).get('logo')
#     Label
#         Text:getattr(self, 'data',{}).get('logo')
