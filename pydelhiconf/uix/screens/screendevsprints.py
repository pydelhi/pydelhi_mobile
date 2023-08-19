from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from network import get_data
from kivy.factory import Factory
from kivy.properties import ObjectProperty


app = App.get_running_app()
    
class devsprint(ScrollView):
    data = ObjectProperty({})

class ScreenDevSprints(Screen):
    Builder.load_string('''

<ScreenDevSprints>
    name: 'ScreenDevSprints'
    
    BoxLayout
        orientation:'vertical'
        id:main
        BackLabel
            backcolor: app.base_inactive_color[:3] + [.5]
            text: "Dev Sprints"        
            pos_hint:{'top':1}
            size_hint:1,None
<devsprint>
    ScrollGrid

        AsyncImage
            source: root.data.get('image',"")
            size_hint_y: None
            allow_stretch: 'image' not in root.data
            height: dp(200)
            mipmap: True
        BackLabel
            text: root.data.get('text1',"")
        BackLabel
            backcolor: 0, 0, 0, 0
            text:root.data.get('text2',"")


''')

    def on_pre_enter(self):
        container = self.ids.main
        container.opacity = 0

    def on_enter(self,onsuccess = False):
        container = self.ids.main
        container.clear_widgets()
        data = get_data('devsprint', onsuccess=onsuccess).get('0.0.1',{})
        main = self.ids.main
        main.add_widget(Factory.devsprint(data=data))
        Factory.Animation(opacity=1, d=.5).start(container)
        
        # devsprint = app.ScreenDevSprints;
        # devsprint.data = data