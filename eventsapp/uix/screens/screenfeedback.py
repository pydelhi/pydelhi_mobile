from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


class ScreenFeedback(Screen):
    Builder.load_string('''
<ScreenFeedback>
    name: 'ScreenFeedback'
    talk: ''
    BoxLayout
        padding: '9dp'
        spacing: '9dp'
        orientation: 'vertical'
        ScrollGrid
            padding: '9dp'
            spacing: '9dp'
            BackLabel
                text: "Feedback for " + root.talk
                backcolor: app.base_active_color[:3] + [.5]
                # size_hint_y: None
                # height: dp(100)
            BoxLayout
                size_hint_y: None
                height: dp(45)
                BackLabel
                    text: 'Rating: {}'.format(sldr.value)
                    size_hint_x: .5
                    pos_hint: {'center_y': .5}
                Slider
                    id: sldr
                    canvas.after:
                        Color:
                            rgba: 1, 1, 1, .9
                        Rectangle:
                            size: self.size
                            pos: self.value_pos[0], self.y
                    cursor_image: 'atlas://data/default/transparent'
                    background_horizontal: 'atlas://data/default/ratingrankin'
                    border_horizontal: 0, 0, 0, 0
                    min: 0
                    max: 10
            TextInput:
                id: ti_name
                size_hint_y: None
                height: dp(45)
                hint_text: 'Your Name here...'
            TextInput:
                id: ti_ticketid
                size_hint_y: None
                height: dp(45)
                hint_text: 'Your Ticket ID...'
        TextInput:
            id: ti_description
            hint_text: 'Enter detailed feedback here...'
        ActiveButton
            text: 'Submit'
            size_hint_y: None
            height: dp(45)
            on_released:
                rating = '{} out of {}'.format(sldr.value, sldr.max)
                title = 'Title: ' + root.talk
                detailed_description = "Description:" + ti_description.text
                name = "Name: " + ti_name.text
                ticketid = "Ticketid: " + ti_ticketid.text
                import webbrowser
                webbrowser.open(\
                "mailto:feedback@in.pycon.org?Subject=TalkFeedback&body" +\
                "={}".format("\\n\\n".join((rating, title, detailed_description\
                , name, ticketid))))
''')

    def on_pre_enter(self):
        self.manager.transition.direction = 'up'

    def on_pre_leave(self):
        self.manager.transition.direction = 'down'

    def on_leave(self):
        self.manager.transition.direction = 'left'
