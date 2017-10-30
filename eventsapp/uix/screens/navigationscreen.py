'''
Navigation Screen
=================
Display a Navigation drawer

-------- ----------------------------------
        | =    PyCon India 2017            |
        |__________________________________
        |                                  |
        |                                  |
        |                                  |
But1    |                                  |
        |     Logo Here                    |
But2    |                                  |
        |                                  |
But3    |       ----------------------     |
        |     [ Workshop + Dev Sprints ]   |
But4    |       ----------------------     |
        |                                  |
But5    |       ----------------------     |
        |     [ Conference Days        ]   |
But6    |       ----------------------     |
        |                                  |
        |                                  |
'''


# from kivy.factory import Factory
# Factory.register('NavigationDrawer', module='uix.navigationdrawer')
from uix.navigationdrawer import NavigationDrawer
from kivy.uix.screenmanager import Screen
from kivy.properties import (ObjectProperty, NumericProperty, OptionProperty,
                             BooleanProperty, StringProperty)
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.app import App

from uix.buttons import ImageButton

import json


class NavButton(Button):
    menu_item_text = StringProperty('')
    icon_source = StringProperty('')
    navigate_to = StringProperty('')


class LeftPanel(BoxLayout):
    Builder.load_string('''
<LeftPanel>
    orientation: 'vertical'
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos
    Image
        id: img_back
        source: "data/images/background.png"
        allow_stretch: True
        keep_ratio: False
        size_hint: 1, None
        height: max(dp(250), 0.25*self.parent.height)
        Image
            source: 'data/images/logo.png'
            size: img_back.width, img_back.height/3.
            center: img_back.center

    RelativeLayout
        size_hint: 1, 1
        BoxLayout
            id: menu_buttons_container
            size_hint: 1, .8
            pos_hint: {'center_y': .55}
            orientation: 'vertical'

    ''')


class TopBar(BoxLayout):

    back_button_image = StringProperty('data/images/hamburger.png')
    title = StringProperty('PyCon India 2017')
    navigate_back = BooleanProperty(False)

    def on_menu_press(self):
        app = App.get_running_app()
        if self.navigate_back:
            manager = app.navigation_screen.ids.nav_manager
            manager.transition.direction = 'right'
            manager.current = 'ScheduleScreen'
        else:
            app.navigationdrawer.toggle_state()


    Builder.load_string('''
<TopBar>
    size_hint: 1, None
    height: dp(50)
    width: dp(45)
    spacing: dp(15)
    canvas.before:
        Color:
            rgba: 69/255., 132/255., 182/255., 1
        Rectangle:
            size: self.size
            pos: self.pos
    ImageButton:
        source: root.back_button_image
        on_release: root.on_menu_press()
    Label:
        text: root.title
        shorten: True
        text_size: self.size
        font_size: dp(22)
        halign: 'left'
        valign: 'center'
    ''')


class NavigationScreen(Screen):

    Builder.load_string('''
<NavButton>
    background_normal: ''
    on_release:
        app.navigation_screen.ids.drawer.toggle_state()
        app.load_screen(root.navigate_to,
        manager=app.navigation_screen.ids.nav_manager)
    StackLayout:
        pos: self.parent.pos
        size: self.parent.size
        orientation: 'lr-tb'
        Image:
            source: root.icon_source
            size_hint_x: None
            width: 0.4*self.parent.width
        Label:
            size_hint_x: None
            text: root.menu_item_text
            text_size: dp(150), None
            halign: 'left'
            valign: 'center'
            font_size: dp(18)
            bold: True
            color: 0, 0, 0, 1

<NavigationScreen>
    name: 'NavigationScreen'
    on_parent: app.navigation_screen = self
    NavigationDrawer
        id: drawer
        anim_type: 'slide_above_simple'
        separator_image_width: dp(0)
        side_panel_width: max(dp(350), 0.8*self.width)
        on_parent: if self.parent: app.navigationdrawer = self
        LeftPanel
            id: leftpanel
        ScreenManager
            id: nav_manager
            on_parent: if self.parent: app.load_screen('WelcomeScreen', manager=self)

    ''')

    def on_pre_enter(self, onsuccess = False):
        menu_container = self.ids.leftpanel.ids.menu_buttons_container
        menu_container.clear_widgets()
        with open('eventsapp/data/jsonfiles/menuitems.json') as data_file:
            data = json.load(data_file)
        menuitems = data.get("0.0.1")
        for item in menuitems:
            bl = Factory.NavButton(navigate_to=item['navigate_to'],
                                   menu_item_text=item['menu_item_text'],
                                   icon_source=item['icon_source'])
            menu_container.add_widget(bl)
