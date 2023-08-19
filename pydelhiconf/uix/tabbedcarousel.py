from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from weakref import ref

class TabbedCarousel(Factory.TabbedPanel):
    '''Custom TabbedPanel using a carousel used in the Main Screen
    '''
    Builder.load_string('''
<TabbedCarousel>
    carousel: carousel
    do_default_tab: False
    Carousel:
        scroll_timeout: 120
        scroll_distance: '20dp'
        anim_type: 'out_quart'
        min_move: .05
        anim_move_duration: .1
        anim_cancel_duration: .54
        on_index: root.on_index(*args)
        id: carousel
''')

    carousel = ObjectProperty(None)

    def animate_tab_to_center(self, value):
        scrlv = self._tab_strip.parent
        if not scrlv:
            return
        idx = self.tab_list.index(value)
        n = len(self.tab_list)
        if idx in [0, 1]:
            scroll_x = 1
        elif idx in [n-1, n-2]:
            scroll_x = 0
        else:
            scroll_x = 1. * (n - idx - 1) / (n - 1)
        mation = Factory.Animation(scroll_x=scroll_x, d=.25)
        mation.cancel_all(scrlv)
        mation.start(scrlv)

    def on_current_tab(self, instance, value):
        self.animate_tab_to_center(value)

    def on_index(self, instance, value):
        current_slide = instance.current_slide
        
        if not hasattr(current_slide, 'tab'):
            return
        tab = current_slide.tab()
        ct = self.current_tab
        try:
            if ct.text != tab.text:
                carousel = self.carousel
                carousel.slides[ct.slide].dispatch('on_leave')
                self.switch_to(tab)
                carousel.slides[tab.slide].dispatch('on_enter')
        except AttributeError:
            current_slide.dispatch('on_enter')

    def switch_to(self, header):
        # we have to replace the functionality of the original switch_to
        if not header:
            return
        if not hasattr(header, 'slide'):
            header.content = self.carousel
            super(TabbedCarousel, self).switch_to(header)
            try:
                tab = self.tab_list[-1]
            except IndexError:
                return
            self._current_tab = tab
            tab.state = 'down'
            return

        carousel = self.carousel
        self.current_tab.state = "normal"
        header.state = 'down'
        self._current_tab = header
        # set the carousel to load  the appropriate slide
        # saved in the screen attribute of the tab head
        slide = carousel.slides[header.slide]
        if carousel.current_slide != slide:
            carousel.current_slide.dispatch('on_leave')
            carousel.load_slide(slide)
            slide.dispatch('on_enter')

    def add_widget(self, widget, index=0):
        if isinstance(widget, Factory.Screen):
            self.carousel.add_widget(widget)
            tp = Factory.TabbedPanelHeader(text=widget.name)
            tp.slide = self.carousel.slides.index(widget)
            widget.tab = ref(tp)
            super(TabbedCarousel, self).add_widget(tp, index=index)
            return
        super(TabbedCarousel, self).add_widget(widget, index=index)

