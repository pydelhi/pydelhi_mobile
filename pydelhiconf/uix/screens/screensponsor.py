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
    data = ObjectProperty(None)
    def popup(self):
        label = Factory.popupLabel(text = self.data['about'])
        popup = Factory.Popup(title=self.data['name'], content=label)
        popup.open()


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

<Sponsor@ButtonBehavior+StackLayout>
    orientation: 'tb-rl'
    spacing: dp(12)
    size_hint: 1, 1
    Label
        text: self.parent.data['name']
        size_hint: 1, None
        height: dp(18)
        font_size:dp(15)
    
    Button:
        text: "more ..."
        size_hint:None,None
        height:dp(10)
        width:dp(50)
        pos_hint:{'right':1}
        font_size:dp(10)
        background_color: (1.0, 0.0, 0.0, 0)

        on_release:
            self.parent.popup()

    AsyncImage
        size_hint:1,.8
        halign: 'center'
        padding: dp(10), dp(10)
        valign: 'middle'
        allow_stretch:False
        source: self.parent.data['logo']
    
    
<popupLabel@Label>
    size_hint:1,1
    padding: dp(5), dp(10)
    font_size: dp(10)
    halign:'left'
    valign:'top'
    text_size: self.width, self.height

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
