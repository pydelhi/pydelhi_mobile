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
        spacing: dp(12)
        orientation: 'vertical'
        Image:
            source: 'atlas://data/default/ticket'
            allow_stretch: True
            size: root.size
            opacity: 1
        BoxLayout
            size_hint_y: None
            height: dp(50)
            spacing: dp(5)
            ActiveButton
                text: 'My tickets'
                on_release:
                    webbrowser.open('http://in.explara.com/a/account/manage/my-orders')
            ActiveButton
                text: 'Buy tickets'
                on_release:
                    webbrowser.open('http://bit.do/pydelhiconf2017tickets')
''')  

    

