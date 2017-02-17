'''Screen Schedule
'''

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.factory import Factory

app = App.get_running_app()


class ScreenSchedule(Screen):
    '''
    FIXME

    '''

    Builder.load_string('''
<Topic@Label>
    canvas.before:
        Color
            rgba: app.base_inactive_light
        Rectangle
            size: dp(300), self.height
            pos: self.right - dp(300), self.y
        Color
            rgba: app.base_inactive_light[:3]+[.5]
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
            rgba: root.back_color or (1, 1, 1, 1)
        Rectangle
            size: dp(270), dp(36)
            pos: self.x, self.top - dp(36)
        Color
            rgba: (list(root.back_color[:3])+[.3]) if root.back_color else (1, 1, 1, 1)
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
            text: app.event_name
        Accordion
            id: accordian_days
            orientation: 'vertical'
            # AccordionItem
            #     back_color: app.base_active_color
            #     title: 'Saturday March 18, 2017'
            #     BoxLayout
            #         ScrollView
            #             id: left_scroll
            #             on_scroll_y: right_scroll.scroll_y = args[1]
            #             size_hint_x: None
            #             width: dp(100)
            #             GridLayout
            #                 cols: 1
            #                 size_hint: 1, None
            #                 height: self.minimum_height
            #                 padding: dp(2)
            #                 spacing: dp(2)
            #                 TimeSlice
            #                 TimeSlice
            #                 TimeSlice
            #                 TimeSlice
            #                 TimeSlice
            #                 TimeSlice
            #                 TimeSlice
            #                 TimeSlice
            #                 TimeSlice
            #                 TimeSlice
            #                 TimeSlice
            #                 TimeSlice
            #                 TimeSlice
            #                 TimeSlice
            #                 TimeSlice
            #         ScrollView
            #             id: right_scroll
            #             on_scroll_y: left_scroll.scroll_y = args[1]
            #             GridLayout
            #                 cols: 1
            #                 size_hint: 1, None
            #                 height: sp(900)
            #                 Button
            #                     height: dp(900)
            #                 Button
            # AccordionItem
            #     back_color: app.base_inactive_light
            #     title: 'Sunday March 19, 2017'
 ''')
    # TODO take schedule from json and display data based on it
    # what's present above is only a simple test


    def on_enter(self):
        
        self.ids.accordian_days.clear_widgets()
        from network import get_data
        # this should update the file on disk
        event = get_data('event')
        schedule = get_data('schedule')
        # read the file from disk

        app.event_name = event['name']
        app.venue_name = event['venue']

        start_date = event['start_date']
        end_date = event['end_date']

        dates = schedule['results'][0].keys()
        
        # See if this would be needed at all
        #
        # from datetime import datetime
        # start_date = datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%SZ')
        # end_date = datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%SZ')
        # days = (end_date - start_date).days + 1
        # dates = schedule['results'][0].keys()
        # print dates, '<<<<'

        # Content to be added to timeslice
        #
        # dates = schedule['results'][0].keys()
        #
        # i=0
        # for date in dates:
        #     schedule['results'][0][date][i]['title']
        #     schedule['results'][0][date][i]['start_time']
        #     schedule['results'][0][date][i]['end_time']
        #     schedule['results'][0][date][i]['type']
        #     schedule['results'][0][date][i]['speaker_name']
        #     i+=1

        for date in dates:
            cday = Factory.AccordionItem(title=date)
            self.ids.accordian_days.add_widget(cday)

            # TODO: Dates are not sorted


