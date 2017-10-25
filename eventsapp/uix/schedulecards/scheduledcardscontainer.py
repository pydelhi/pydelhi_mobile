'''
Schedule Cards Container:
================

'''

from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout


class ScheduleScrollContainer(ScrollView):
    '''
    Thanks to kivymd for making scrolling easy.
    Code inspired from https://groups.google.com/forum/?fromgroups=#!topic/kivy-users/AiaUnKp3XX4
    '''
    def __init__(self, *args, **kwargs):
        kwargs['do_scroll_x'] = False
        super(ScheduleScrollContainer, self).__init__(*args, **kwargs)
        self._grid_widget = ScheduleCardsContainer()
        super(ScheduleScrollContainer, self).add_widget(self._grid_widget)
    @property
    def childs(self):
        return self._grid_widget.children
    def add_widget(self, widget, index=0):
        self._grid_widget.add_widget(widget, index=0)
    def del_widget(self, widget):
        self._grid_widget.del_widget(widget)


class ScheduleCardsContainer(GridLayout):
    _bind = True
    def __init__(self, *args, **kwargs):
        kwargs['size_hint_y'] = None
        kwargs['cols'] = 1
        super(ScheduleCardsContainer, self).__init__(*args, **kwargs)
    def add_widget(self, widget, index=0):
        if self._bind:
            self.bind(minimum_height=self.setter('height'))
            self._bind = False
        super(ScheduleCardsContainer, self).add_widget(widget, index)
        self.height += widget.height
    def del_widget(self, widget):
        super(ScheduleCardsContainer, self).del_widget(widget)
        self.height -= wigdet.height

    Builder.load_string('''
<ScheduleCardsContainer>:
    spacing: dp(10)
    padding: dp(20), dp(40)
    canvas:
        Color:
            rgba: (1, 1, 1, 1)
        Rectangle:
            size: self.size
            pos: self.pos
    ''')
