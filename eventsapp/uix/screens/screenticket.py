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
        AsyncImage:
            source: 'https://www.wwkd.org/wp-content/uploads/2018/08/tickets.png'
            allow_stretch: True
            size: root.size
            opacity: 1
        BoxLayout
            size_hint_y: None
            height: dp(36)
            spacing: dp(5)
            ActiveButton
                text: 'My tickets'
                on_release:
                    webbrowser.open(\
                    'http://in.explara.com/a/account/manage/my-orders')
            ActiveButton
                text: 'Buy tickets'
                disabled: True
                on_touch_down: self.text = 'Sold Out'
                # on_release:
                #     webbrowser.open('http://bit.do/pyconf2018tickets')
''')
