'''
logo_screen:
=============
Display the logo
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

class LogoScreen(Screen):

   Builder.load_string('''
<LogoScreen>
    name: 'LogoScreen'
    on_enter:
        from kivy.animation import Animation
        anim = Animation(opacity=1, size=(root.width - dp(90), root.height), d=.5)
        anim.bind(on_complete=lambda *args: app.load_screen('NavigationScreen'))
        anim.start(logo_img)
    Image
        source: 'data/images/background.png'
        allow_stretch: True
        keep_ratio: False
    Image
    	id: logo_img
    	opacity: 0
    	mipmap: True
    	source: 'data/images/logo.png'
    	allow_stretch: True
    	size_hint: None, None
    	size: 0, 0
    	pos_hint: {'center_x': .5, 'center_y': .5}
 ''')
