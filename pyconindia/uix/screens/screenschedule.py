'''Screen Schedule
'''


from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from uix.tabbedcarousel import TabbedCarousel


class ScreenSchedule(Screen):
    '''
     ----------------------------------------
    |             Pycon India 2016        v  |
     ----------------------------------------
    |   September 23rd Friday Workshop Day   |
     ----------------------------------------
    |Timings:     |  Hall 1       | Hall 2   | Hall 3 |
    |----------------------------------------|
    |9:00 -  10:00| Keynote       |          |
    |10:00 - 12:00| Workshop 1    |          |
    |12:00 - 02:00| Workshop 2    |          |
    |02:00 - 03:00| Lunch         |          |
    |03:00 - 05:00| Workshop 3    |          |
    |----------------------------------------|
    |   September 24th Saturday Conf Day 1   |
    |----------------------------------------|
    |   September 24th Saturday Conf Day 2   |
     ----------------------------------------

    '''

    Builder.load_string('''
<Topic@Label>
    canvas.before:
        Color
            rgba: 45/256, 191/256., 212/256., 1
        Rectangle
            size: dp(300), self.height
            pos: self.right - dp(300), self.y
        Color
            rgba: 45/256, 191/256., 212/256., .5
        Rectangle
            size: dp(300), self.height
            pos: self.right - dp(310), self.y - dp(10)
    font_size: dp(27)
    text_size: self.width - dp(10), self.height
    size_hint_y: None
    height: dp(50)
    halign: 'right'
    valign: 'middle'
    text: 'Hello World'

<AccordionItemTitle>
    text_size: self.width - dp(10), self.height
    halign: 'left'
    valign: 'middle'

<AccordionItem>
    back_color: app.base_active_color
    canvas.before:
        Color
            rgba: root.back_color if root.back_color else (1, 1, 1, 1)
        Rectangle
            size: dp(270), dp(36)
            pos: self.x, self.top - dp(36)
        Color
            rgba: (list(root.back_color[:3]) + [.3]) if root.back_color else (1, 1, 1, 1)
        Rectangle
            size: dp(270), dp(36)
            pos: self.x + dp(7), self.top - (dp(36) + dp(7))
    

<TimeSlice@Label>
    text: '00:00 - 00:00'
    size_hint_y: None
    height: dp(27)
    background_color: app.base_active_color[:3] + [.3]
    canvas.before:
        Color
            rgba: root.background_color if root.background_color else (1, 1, 1, 1)
        Rectangle
            size: self.size
            pos: self.pos

<TimeSliceD1@TimeSlice>
    background_color: 

<ScreenSchedule>
    name: 'ScreenSchedule'
    on_enter:
        # from utils import fetch_data
        # fetch_data()
    BoxLayout
        spacing: dp(20)
        orientation: 'vertical'
        padding: dp(4)
        Topic
            text: 'PyCon India 2016'
        Accordion
            id: accordian_days
            orientation: 'vertical'
            AccordionItem
                back_color: app.base_active_color
                title: 'Friday September 23 2016'
                BoxLayout
                    ScrollView
                        id: left_scroll
                        on_scroll_y: right_scroll.scroll_y = args[1]
                        size_hint_x: None
                        width: dp(100)
                        GridLayout
                            cols: 1
                            size_hint: 1, None
                            height: self.minimum_height
                            padding: dp(2)
                            spacing: dp(2)
                            TimeSlice
                            TimeSlice
                            TimeSlice
                            TimeSlice
                            TimeSlice
                            TimeSlice
                            TimeSlice
                            TimeSlice
                            TimeSlice
                            TimeSlice
                            TimeSlice
                            TimeSlice
                            TimeSlice
                            TimeSlice
                            TimeSlice
                    ScrollView
                        id: right_scroll
                        on_scroll_y: left_scroll.scroll_y = args[1]
                        GridLayout
                            cols: 1
                            size_hint: 1, None
                            height: sp(900)
                            Button
                                height: dp(900)
                            Button

            AccordionItem
                back_color: app.base_inactive_color
                title: 'Saturday September 24 2016'
            AccordionItem
                back_color: 45/256, 191/256., 212/256., 1
                title: 'Sunday September 25 2016'
 ''')