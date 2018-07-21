'''
Cards Container:
================

'''

from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.app import App


class ScrollableCardContainer(ScrollView):
    '''
    Thanks to kivymd for making scrolling easy.
    Code inspired from https://groups.google.com/forum/?fromgroups=#!topic/kivy-users/AiaUnKp3XX4
    '''
    def __init__(self, *args, **kwargs):
        kwargs['do_scroll_x'] = False
        super(ScrollableCardContainer, self).__init__(*args, **kwargs)
        self._grid_widget = CardsContainer()
        super(ScrollableCardContainer, self).add_widget(self._grid_widget)
    @property
    def childs(self):
        return self._grid_widget.children
    def add_widget(self, widget, index=0):
        self._grid_widget.add_widget(widget, index=0)
    def del_widget(self, widget):
        self._grid_widget.del_widget(widget)


class CardsContainer(GridLayout):
    _bind = True
    def __init__(self, *args, **kwargs):
        kwargs['size_hint_y'] = None
        kwargs['cols'] = 1
        super(CardsContainer, self).__init__(*args, **kwargs)
    def add_widget(self, widget, index=0):
        if self._bind:
            self.bind(minimum_height=self.setter('height'))
            self._bind = False
        super(CardsContainer, self).add_widget(widget, index)
        self.height += widget.height
    def del_widget(self, widget):
        super(CardsContainer, self).del_widget(widget)
        self.height -= wigdet.height

    Builder.load_string('''
<CardsContainer>:
    spacing: dp(10)
    padding: dp(10), dp(10)
    canvas:
        Color:
            rgba: (1, 1, 1, 1)
        Rectangle:
            size: self.size
            pos: self.pos
    ''')


class CardBoxLayout(BoxLayout):

    Builder.load_string('''
<CardBoxLayout>:
    orientation: 'vertical'
    padding: dp(20), dp(10)
    spacing: dp(40)
    canvas:
        Color:
            rgba: (.91, .91, .91, 1)
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [dp(10)]
        Color:
            rgba: (0, 0, 0, 1)
            a: 1
        Line:
            rounded_rectangle: (self.pos[0],self.pos[1],self.size[0],self.size[1], 10)
    ''')

class CardStackLayout(StackLayout):

    Builder.load_string('''
<CardStackLayout>:
    pos: self.parent.pos
    size: self.parent.size
    orientation: 'lr-tb'
    padding: dp(20), dp(10)
    spacing: dp(40)
    canvas:
        Color:
            rgba: (.91, .91, .91, 1)
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [dp(10)]
        Color:
            rgba: (0, 0, 0, 1)
            a: 1
        Line:
            rounded_rectangle: (self.pos[0],self.pos[1],self.size[0],self.size[1], 10)
    ''')
