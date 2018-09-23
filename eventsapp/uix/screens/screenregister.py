from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
# from kivy.app import App


class ScreenRegister(Screen):
    Builder.load_string('''
<ScreenRegister>
    name: 'ScreenRegister'
    data_file_dir: 'data/registeration'
    GridLayout
        size_hint: .5, None
        height: self.minimum_height
        pos_hint: {'center_x': .5, 'center_y': .5}
        spacing: dp(9)
        cols: 1
        BoxLayout
            size_hint_y: None
            height: dp(45)
            BackLabel
                text: 'data file dir'
            ActiveButton:
                text: root.data_file_dir
                on_release: pass

''')

    def on_enter(self):
        # read csv file here
        # import csv
        # with open('/Users/quanon/Downloads/buyers-172227.csv.xls', 'rb') as csvfile:
        #     spamreader = csv.reader(csvfile, dialect='excel')
        #     for row in spamreader:
        #         print(','.join(row))
        #         break
        pass

    def register_attendee(self):
        pass

    def scan_qrcode(self):
        pass
