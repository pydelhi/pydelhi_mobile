#!python

"""
AndroidTabs
===========
AndroidTabs try to reproduce the behaviours of Android Tabs.
It allow you to create your own custom tabbed panel
with an animated tab indicator in a easy way.
Just create your tabs that must inherit from AndroidTabsBase
and add them to an AndroidTabs instance.

class MyTab(BoxLayout, AndroidTabsBase):

    pass

android_tabs = AndroidTabs()

for n in range(1,6):

    tab = MyTab(text='Tab %s' % n)
    tab.add_widget(Button(text='Button %s' % n))
    android_tabs.add_widget(tab)
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.carousel import Carousel
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle
from kivy.utils import boundary
from kivy.properties import (
    ObjectProperty,
    NumericProperty,
    VariableListProperty,
    StringProperty,
    AliasProperty,
    BooleanProperty,
    BoundedNumericProperty,
    ReferenceListProperty
)


class AndroidTabsException(Exception):
    '''The AndroidTabsException class'''
    pass


class AndroidTabsLabel(ToggleButtonBehavior, Label):
    '''
    AndroidTabsLabel it represent the label of each tab.
    '''

    text_color_normal = VariableListProperty([1, 1, 1, .6])
    '''
    Text color of the label when it is not selected.
    '''

    text_color_active = VariableListProperty([1])
    '''
    Text color of the label when it is selected.
    '''

    tab = ObjectProperty(None)
    tab_bar = ObjectProperty(None)

    def __init__(self, **kwargs):

        super(AndroidTabsLabel, self).__init__(**kwargs)
        self.min_space = 0

    def on_release(self):
        # if the label is selected load the relative tab from carousel
        if self.state == 'down':
            self.tab_bar.parent.carousel.load_slide(self.tab)

    def on_texture(self, widget, texture):
        # just save the minimum width of the label based of the content
        if texture:
            self.width = texture.width
            self.min_space = self.width

    def _trigger_update_tab_indicator(self):
        # update the position and size of the indicator
        # when the label changes size or position
        if self.state == 'down':
            self.tab_bar.update_indicator(self.x, self.width)


class AndroidTabsBase(Widget):

    '''
    AndroidTabsBase allow you to create a tab.
    You must create a new class that inherits
    from AndroidTabsBase.
    In this way you have total control over the
    views of your tabbed panel.
    '''

    text = StringProperty('')
    '''
    It will be the label text of the tab.
    '''

    tab_label = ObjectProperty(None)
    '''
    It is the label object reference of the tab.
    '''

    def __init__(self, **kwargs):

        self.tab_label = AndroidTabsLabel(tab=self)
        super(AndroidTabsBase, self).__init__(**kwargs)

    def on_text(self, widget, text):
        # set the label text
        self.tab_label.text = self.text


class AndroidTabsMain(BoxLayout):
    '''
    AndroidTabsMain is just a boxlayout that contain
    the carousel. It allows you to have control over the carousel.
    '''
    pass


class AndroidTabsCarousel(Carousel):
    '''
    AndroidTabsCarousel class.
    '''
    pass


class AndroidTabsScrollView(ScrollView):
    '''
    AndroidTabsScrollView hacked version to fix scroll_x manual setting.
    '''
    def goto(self, scroll_x, scroll_y):
        ''' Update event value along with scroll_*
        '''
        def _update(e, x):
            if e:
                e.value = (e.max + e.min) * x

        if not (scroll_x is None):
            self.scroll_x = scroll_x
            _update(self.effect_x, scroll_x)

        if not (scroll_y is None):
            self.scroll_y = scroll_y
            _update(self.effect_y, scroll_y)


class AndroidTabsBar(BoxLayout):
    '''
    AndroidTabsBar is just a boxlayout that contain
    the scrollview for the tabs.
    It is also responsible to resize the tab label when it needed.
    '''

    target = ObjectProperty(None, allownone=True)
    '''
    Is the carousel reference of the next tab / slide.
    When you go from "Tab A" to "Tab B", "Tab B" will be the
    target tab / slide of the carousel.
    '''

    def get_rect_instruction(self):

        for i in self.layout.canvas.after.children:
            if isinstance(i, Rectangle):
                return i

    indicator = AliasProperty(
        get_rect_instruction,
        cache=True)
    '''
    Is the Rectangle instruction reference
    of the tab indicator.
    '''

    def get_last_scroll_x(self):

        return self.scrollview.scroll_x

    last_scroll_x = AliasProperty(
        get_last_scroll_x,
        bind=('target', ),
        cache=True)
    '''
    Is the carousel reference of the next tab / slide.
    When you go from "Tab A" to "Tab B", "Tab B" will be the
    target tab / slide of the carousel.
    '''

    def __init__(self, **kwargs):
        self._trigger_update_tab_bar = Clock.schedule_once(
            self._update_tab_bar, 0)
        super(AndroidTabsBar, self).__init__(**kwargs)

    def _update_tab_bar(self, *args):
        # update width of the labels when it is needed
        width, tabs = self.scrollview.width, self.layout.children
        tabs_widths = [t.min_space for t in tabs if t.min_space]
        tabs_space = float(sum(tabs_widths))

        if not tabs_space:
            return

        ratio = width / tabs_space
        use_ratio = True in (width / len(tabs) < w for w in tabs_widths)

        for t in tabs:

            t.width = t.min_space if tabs_space > width \
                        else t.min_space * ratio if use_ratio is True \
                        else width / len(tabs)

    def update_indicator(self, x, w):
        # update position and size of the indicator
        self.indicator.pos = (x, 0)
        self.indicator.size = (w, self.indicator.size[1])

    def tab_bar_autoscroll(self, target, step):
        # automatic scroll animation of the tab bar.
        bound_left = self.center_x
        bound_right = self.layout.width - bound_left
        dt = target.center_x - bound_left
        sx, sy = self.scrollview.convert_distance_to_scroll(dt, 0)

        # last scroll x of the tab bar
        lsx = self.last_scroll_x

        # determine scroll direction
        scroll_is_late = lsx < sx

        # distance to run
        dst = abs(lsx - sx) * step

        if not dst:
            return

        if scroll_is_late and target.center_x > bound_left:
            x = lsx + dst

        elif not scroll_is_late and target.center_x < bound_right:
            x = lsx - dst
        
        x = boundary(x, 0.0, 1.0)
        self.scrollview.goto(x, None)


    def android_animation(self, carousel, offset):
        # try to reproduce the android animation effect.
        if offset != 0 and abs(offset) < carousel.width:
            forward = offset < 0
            offset = abs(offset)
            step = offset / float(carousel.width)
            distance = abs(offset - carousel.width)
            threshold = self.parent.anim_threshold
            breakpoint = carousel.width - (carousel.width * threshold)
            traveled = distance / breakpoint if breakpoint else 0
            break_step = 1.0 - traveled
            indicator_animation = self.parent.tab_indicator_anim

            skip_slide = carousel.slides[carousel._skip_slide] \
                            if carousel._skip_slide is not None else None
            next_slide = carousel.next_slide \
                            if forward else carousel.previous_slide
            self.target = skip_slide if skip_slide else next_slide

            if not self.target:
                return

            a = carousel.current_slide.tab_label
            b = self.target.tab_label

            self.tab_bar_autoscroll(b, step)

            if not indicator_animation:
                return

            if step <= threshold:

                if forward:
                    gap_w = abs((a.x + a.width) - (b.x + b.width))
                    w_step = a.width + (gap_w * step)
                    x_step = a.x

                else:
                    gap = abs((a.x - b.x))
                    x_step = a.x - gap * step
                    w_step = a.width + gap * step

            else:

                if forward:
                    x_step = a.x + abs((a.x - b.x)) * break_step
                    gap_w = abs((a.x + a.width) - (b.x + b.width))
                    ind_width = a.width + gap_w * threshold
                    gap_w = ind_width - b.width
                    w_step = ind_width - (gap_w * break_step)

                else:
                    x_step = a.x - abs((a.x - b.x)) * threshold
                    x_step = x_step - abs(x_step - b.x) * break_step
                    ind_width = (a.x + a.width) - x_step if threshold else a.width
                    gap_w = ind_width - b.width
                    w_step = ind_width - (gap_w * break_step)
                    w_step = w_step if w_step + x_step <= a.x + a.width \
                                                            else ind_width

            self.update_indicator(x_step, w_step)


class AndroidTabs(AnchorLayout):
    '''
    The AndroidTabs class.
    You can use it to create your own custom tabbed panel.
    '''

    default_tab = NumericProperty(0)
    '''
    Index of the default tab. Default to 0.
    '''

    tab_bar_height = NumericProperty('48dp')
    '''
    Height of the tab bar.
    '''

    tab_indicator_anim = BooleanProperty(True)
    '''
    Tab indicator animation. Default to True.
    If you do not want animation set it to False.
    '''

    tab_indicator_height = NumericProperty('2dp')
    '''
    Height of the tab indicator.
    '''

    tab_indicator_color = VariableListProperty([1])
    '''
    Color of the tab indicator.
    '''

    anim_duration = NumericProperty(0.2)
    '''
    Duration of the slide animation. Default to 0.2.
    '''

    anim_threshold = BoundedNumericProperty(
        0.8, min=0.0, max=1.0,
        errorhandler=lambda x: 0.0 if x < 0.0 else 1.0)
    '''
    Animation threshold allow you to change
    the tab indicator animation effect.
    Default to 0.8.
    '''

    def on_carousel_index(self, carousel, index):
        # when the index of the carousel change, update
        # tab indicator, select the current tab and reset threshold data.
        current_tab_label = carousel.current_slide.tab_label
        if current_tab_label.state == 'normal':
            current_tab_label._do_press()
        self.tab_bar.update_indicator(
            current_tab_label.x,
            current_tab_label.width)

    def add_widget(self, widget):
        # You can add only subclass of AndroidTabsBase.
        if len(self.children) >= 2:

            if not issubclass(widget.__class__, AndroidTabsBase):
                raise AndroidTabsException(
                    'AndroidTabs accept only subclass of AndroidTabsBase')

            widget.tab_label.tab_bar = self.tab_bar
            self.tab_bar.layout.add_widget(widget.tab_label)
            self.carousel.add_widget(widget)
            return

        return super(AndroidTabs, self).add_widget(widget)

    def remove_widget(self, widget):
        # You can remove only subclass of AndroidTabsBase.
        if not issubclass(widget.__class__, AndroidTabsBase):

            raise AndroidTabsException(
                'AndroidTabs can remove only subclass of AndroidTabBase')

        if widget.parent.parent == self.carousel:

            self.tab_bar.layout.remove_widget(widget.tab_label)
            self.carousel.remove_widget(widget)


Builder.load_string('''
#:import DampedScrollEffect kivy.effects.dampedscroll.DampedScrollEffect

<AndroidTabsLabel>:
    size_hint: None, 1
    halign: 'center'
    padding: '12dp', 0
    group: 'tabs'
    allow_no_selection: False
    text_color_normal: 1, 1, 1, .6
    text_color_active: 1, 1, 1, 1
    color: self.text_color_active if self.state is 'down' \
                                else self.text_color_normal
    on_x: self._trigger_update_tab_indicator()
    on_width: self._trigger_update_tab_indicator()

<AndroidTabsScrollView>:
    size_hint: 1, 1
    do_scroll_y: False
    bar_color: 0, 0, 0, 0
    bar_inactive_color: 0, 0, 0, 0
    bar_width: 0
    effect_cls: DampedScrollEffect

<AndroidTabs>:
    carousel: carousel
    tab_bar: tab_bar
    anchor_y: 'top'

    AndroidTabsMain:
        padding: 0, tab_bar.height, 0, 0

        AndroidTabsCarousel:
            id: carousel
            anim_move_duration: root.anim_duration
            on_index: root.on_carousel_index(*args)
            on__offset: tab_bar.android_animation(*args)
            on_slides: self.index = root.default_tab
            on_slides: root.on_carousel_index(self, 0)

    AndroidTabsBar:
        id: tab_bar
        carousel: carousel
        scrollview: scrollview
        layout: layout
        size_hint: 1, None
        height: root.tab_bar_height

        AndroidTabsScrollView:
            id: scrollview
            on_width: tab_bar._trigger_update_tab_bar()

            GridLayout:
                id: layout
                rows: 1
                size_hint: None, 1
                width: self.minimum_width
                on_width: tab_bar._trigger_update_tab_bar()

                canvas.after:
                    Color:
                        rgba: root.tab_indicator_color
                    Rectangle:
                        pos: self.pos
                        size: 0, root.tab_indicator_height
''')

kvdemo = '''
#:import get_color_from_hex kivy.utils.get_color_from_hex

<AndroidTabsBar>:
    canvas.before:
        Color:
            rgba: get_color_from_hex('#03A9F4')
        Rectangle:
            pos: self.pos
            size: self.size

        # you can add a bit of shade if you want
        Color:
            rgba: 0,0,0,.3
        Rectangle:
            pos: self.pos[0], self.pos[1] - 1
            size: self.size[0], 1
        Color:
            rgba: 0,0,0,.2
        Rectangle:
            pos: self.pos[0], self.pos[1] - 2
            size: self.size[0], 1
        Color:
            rgba: 0,0,0,.05
        Rectangle:
            pos: self.pos[0], self.pos[1] - 3
            size: self.size[0], 1
<MyTab>:
    Button:
        text: root.text
'''

if __name__ == '__main__':

    class MyTab(BoxLayout, AndroidTabsBase):

        pass

    class Example(App):

        def build(self):

            Builder.load_string(kvdemo)
            android_tabs = AndroidTabs()

            for n in range(1, 6):
                tab = MyTab(text='TAB %s' % n)
                android_tabs.add_widget(tab)

            return android_tabs

    Example().run()
