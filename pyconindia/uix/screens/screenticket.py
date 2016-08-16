'''Ticket:
Display the explara link for the ticket page.
'''
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

class ScreenTicket(Screen):


    Builder.load_string('''
    #:import webbrowser webbrowser
<ScreenTicket>
    name: 'ScreenTicket'
    BoxLayout
        padding: dp(12)
        orientation: 'vertical'
        spacing:dp(5)
        Image:
            source: 'atlas://data/default/ticket'
            allow_stretch: True
            keep_ratio: False
            size: root.size
            opacity: 1
        BoxLayout
            size_hint_y: None
            height: dp(50)
            PyConButton
                text: 'My tickets'
                size_hint_y: None
                group: 'tickets'
                height: dp(54)
                on_released:
                    webbrowser.open('http://in.explara.com/a/account/manage/my-orders')
            PyConButton
                default: True
                group: 'tickets'
                text: 'Buy tickets'
                size_hint_y: None
                height: dp(54)
                on_release:
                    webbrowser.open('https://in.explara.com/e/pycon-india-2016')
''')  

    

