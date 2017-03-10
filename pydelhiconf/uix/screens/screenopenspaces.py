from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


class ScreenOpenSpaces(Screen):
	Builder.load_string('''
<BackLabel@Background+Label>
    valign: 'middle'
    size_hint_y: None
    height: (self.texture_size[1] + dp(9)) if self.text else 0
    backcolor: (226/255.,168/255.,180/255., 0.5)
    text_size: self.width - dp(9), None   
    halign: 'center'    

<ScreenOpenSpaces>
    name: 'ScreenOpenSpaces'
    ScrollView
        GridLayout
            cols: 1
            size_hint_y: None
            height: self.minimum_height
            orientation: 'vertical'
            padding: dp(9)
            BackLabel
                text: "Open Space is the only process that focuses on expanding time and space for the force of self-organisation to do its thing. Although one can't predict specific outcomes, it's always highly productive for whatever issue people want to attend to. Some of the inspiring side effects that are regularly noted are laughter, hard work which feels like play, surprising results and fascinating new questions. \\n-Michael M Pannwitz, Open Space practitioner"
            BackLabel
                backcolor: 0, 0, 0, 0
                text: "The best part about attending any meetups or conferences is getting a chance to converse with people with similar interests. Know about their domains of expertise, tell them about yours and if the interests meet up, collaborate for any future projects/prospects. Open Spaces are exactly for providing such environment for you. So go ahead, find a place, interact with people and make the best of this conference. Have a great time!"
        ''')