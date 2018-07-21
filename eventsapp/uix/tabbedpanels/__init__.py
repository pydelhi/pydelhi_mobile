'''
Tabbed Panels:
=============

'''

from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.lang import Builder
from kivy.properties import ObjectProperty


class DateTabbedPanelItem(TabbedPanelItem):

    Builder.load_string('''
<DateTabbedPanelItem>
    canvas:
        Color:
            rgba: (1, 1, 1, 1) if self.state == 'down' else (69/255., 132/255., 182/255., 1)
        Rectangle:
            size: self.size[0]*.2, self.size[1]*.1
            pos: self.pos[0] + (self.size[0]*.5)/2, self.pos[1]
    background_down: 'data/images/Detail_bar.png'
    background_normal: 'data/images/Detail_bar.png'
    bold: True
    font_size: dp(15)
    ''')


class DateTabbedPanel(TabbedPanel):

    Builder.load_string('''

<DateTabbedPanel>:
    do_default_tab: False
    tab_pos: "top_mid"
    tab_width: self.width/2
    tab_height: dp(40)
    spacing: dp(-5)
    canvas:
        Color:
            rgba: (69/255., 132/255., 182/255., 1)
        Rectangle:
            size: self.size
            pos: self.pos

    ''')


class HallTabbedPanelItem(TabbedPanelItem):
    Builder.load_string('''
<HallTabbedPanelItem>
    canvas:
        Color:
            rgba: (1, 1, 1, 1) if self.state == 'down' else (0, 0, 0, 1)
        Rectangle:
            size: self.size[0]*.5, self.size[1]*.06
            pos: self.pos[0] + (self.size[0]*.5)/2, self.pos[1]
    background_down: 'data/images/lower-detail-bar.png'
    background_normal: 'data/images/lower-detail-bar.png'
    bold: True
    font_size: dp(14)
    ''')


class HallTabbedPanel(TabbedPanel):
    Builder.load_string('''
<HallTabbedPanel>:
    do_default_tab: False
    tab_pos: "bottom_mid"
    tab_width: self.width/3
    tab_height: dp(40)

    ''')
