from kivy.factory import Factory
from kivy.app import App
from kivy.properties import StringProperty
from kivy.lang import Builder
import csv
import os
import json


app = App.get_running_app()
from kivy.config import ConfigParser

config = ConfigParser()
config.read('myconfig.ini')

config.adddefaultsection('pycon2018')
config.setdefault('pycon2018', 'register_data_dir', 'data')


class ScreenRegister(Factory.Screen):

    _data = {}
    '''Holds the data in :attr:`data_file_dir` was processed or not.
    :attr:`_data` is a :type:`String`, defaults to False.
    '''

    data_file_dir = StringProperty(config.get(
        'pycon2018', 'register_data_dir'))
    '''This is the data dir where the registeration data is stored.
    All csv files should be present in this folder.

    :attr:`data_file_dir` is a :class:`~kivy.properties.StringProperty`

    defaults to `data/registeration/`
    '''

    Builder.load_string('''
#:import Factory kivy.factory.Factory
<RSpinner@Spinner>
    background_normal: 'atlas://data/default/spinner'
    background_down: 'atlas://data/default/spinner'
    color: app.base_active_color
    background_color: app.base_active_color if self.state == 'normal' else (1, 1, 1, 1)
    option_cls: Factory.ActiveButton

<ScreenRegister>
    name: 'ScreenRegister'
    on_enter: self._row = ''
    BoxLayout:
        orientation: 'vertical'
        pos_hint: {'center_x': .5}
        padding: dp(9), dp(9)
        spacing: dp(9)
        GridLayout
            size_hint: 1, None
            height: self.minimum_height
            spacing: dp(9)
            cols: 1
            BackLabel
                text: 'Load Registration Data'
                backcolor: app.base_active_color[:3] + [.5]
            BoxLayout
                size_hint_y: None
                height: dp(30)
                spacing: dp(9)
                BackLabel
                    text: root.data_file_dir
                    pos_hint: {'center_x': .5, 'center_y': .5}
                ActiveButton:
                    height: dp(30)
                    text: 'Change...'
                    width: dp(100)
                    size_hint_x: None
                    pos_hint: {'center_y': .5}
                    on_release: root.show_file_chooser()
            # BackLabel
            #     text: 'Restrict attendence from'
            #     backcolor: app.base_active_color[:3] + [.5]
            # BoxLayout
            #     size_hint_y: None
            #     height: dp(30)
            #     spacing: dp(9)
            #     RSpinner:
            #         id: rs1
            #         text: 'A'
            #         values: [chr(x) for x in range(65,91)]
            #         on_text:
            #             if ord(args[1]) > ord(rs2.text):\
            #             self.text = 'A'; rs2.text = 'Z'
            #     RSpinner:
            #         id: rs2
            #         text: 'z'
            #         values: [chr(x) for x in range(65,91)]
            #         on_text:
            #             if ord(args[1]) < ord(rs1.text):\
            #             self.text = 'Z'; rs1.text = 'A'
        BoxLayout
            size_hint_y: None
            height: dp(30)
            spacing: dp(9)
            TextInput:
                id: ti
                write_tab: False
                multiline: False
                background_active: 'atlas://data/default/ti_white'
                background_normal: 'atlas://data/default/ti_white'
                background_color: app.base_active_color
                hint_text: 'Registration Number'
                input_type: 'number'
                input_filter: 'int'
                on_text_validate: bt_check.trigger_action()
            ActiveButton:
                id: bt_check
                height: dp(30)
                text: "Check..."
                size_hint_x: None
                width: dp(100)
                pos_hint: {'center_y': .5}
                on_release: root.check_attendee(ti.text)
        BackLabel
            text: 'Registration Details'
            backcolor: app.base_active_color[:3] + [.5]
        ScrollView
            GridLayout
                padding: dp(9)
                size_hint: 1, None
                height: self.minimum_height
                spacing: dp(13)
                cols: 1
                BackLabel
                    id: lbl_name
                    text: 'Name: '
                BackLabel
                    id: lbl_tshirt
                    text: 'TShirt Size: '
                BackLabel
                    id: lbl_category
                    text: 'Category: '
                BackLabel
                    id: lbl_tickettype
                    text: 'Ticket Type: '
                BoxLayout
                    size_hint_y: None
                    height: lbl_category.height
                    BackLabel
                        text: 'Registered ?'
                    ImBut
                        id: but_registered
                        size_hint_x: None
                        width: dp(54)
                        color: 1, 1, 1, 1
                        source: 'atlas://data/default/close'
                        on_release: if root._row: root.register_user(self)
                BoxLayout
                    size_hint_y: None
                    height: lbl_category.height
                    BackLabel
                        text: 'Swag Distributed ?'
                    ImBut
                        id: but_swag
                        size_hint_x: None
                        width: dp(54)
                        color: 1, 1, 1, 1
                        source: 'atlas://data/default/close'
                        on_release: if root._row: root.distribute_swag(self)
                BoxLayout
                    size_hint_y: None
                    height: lbl_category.height
                    BackLabel
                        text: 'T-Shirt Distributed ?'
                    ImBut
                        id: but_tshirt
                        size_hint_x: None
                        width: dp(54)
                        color: 1, 1, 1, 1
                        source: 'atlas://data/default/close'
                        on_release: if root._row: root.distribute_tshirt(self)
        ActiveButton
            text: 'Start Scanner'
            height: dp(30)
            on_release:
                from utils import scan_qr
                scan_qr(on_complete=root.check_attendee)
''')

    def on_enter(self):
        if not self._data:
            self.on_data_file_dir(self, self.data_file_dir)

    def show_file_chooser(self):
        # update data_file_dir here
        pop = Builder.load_string('''
Popup
    title: 'Select data flie dir'
    BoxLayout
        padding: dp(9)
        spacing: dp(20)
        orientation: 'vertical'
        FileChooserIconView
            id: fl
            filters: ['*.']
            path: '/mnt/sdcard/'
            # dirselect: True
            #filter_dirs: True
        BoxLayout
            spacing: dp(9)
            size_hint_y: None
            height: dp(36)
            ActiveButton
                text: 'Select'
                on_release:
                    app.screenregister.data_file_dir = fl.path
                    root.dismiss()
            ActiveButton
                text: 'Cancel'
                on_release: root.dismiss()
''')
        pop.ids.fl.path = self.data_file_dir
        pop.open()

    def on_data_file_dir(self, instance, data_file_dir):
        # read csv file here
        if not os.path.exists(data_file_dir):
            return
        config.set('pycon2018', 'register_data_dir', data_file_dir)
        config.write()
        _data = {}
        for fl in os.listdir(data_file_dir):
            if not fl.endswith('.csv'):
                continue
            with open(os.sep.join([data_file_dir, fl]), 'rb') as csvfile:
                first_row = True
                spamreader = csv.reader(csvfile, dialect='excel')
                ridx = 0
                for row in spamreader:
                    if first_row:
                        first_row = False
                        idx = row.index('Registration No')
                        continue
                    ridx = row[idx]
                    _data[ridx] = {}
                    _data[ridx]['data'] = row
        self._data = _data

    def check_attendee(self, attendee_data):
        self.ids.ti.text = attendee_data
        _data = self._data
        if attendee_data not in _data:
            self._record_not_found()
            return
        # Records Found
        self._show_record(_data[attendee_data])

    def _record_not_found(self):
        # clear all data
        self.ids.lbl_name.text = 'Record not found'
        self.ids.lbl_name.backcolor = app.base_active_bright[:3] + [.3]
        self.ids.lbl_name.text = 'Name: '
        self.ids.lbl_tshirt.text = 'T-Shirt Size: '
        self.ids.lbl_category.text = 'Category: '
        self.ids.lbl_tickettype.text = 'Ticket Type: '
        self.ids.but_swag.source = 'atlas://data/default/close'
        self.ids.but_registered.source = 'atlas://data/default/close'
        self.ids.but_tshirt.source = 'atlas://data/default/close'
        self._row = ''

    def _show_record(self, record):
        # display the data in record on screen
        self.ids.lbl_name.backcolor = app.base_inactive_color[:3] + [.3]
        self._row = row = record['data']
        self.ids.lbl_name.text = 'Name: {}'.format(row[3])
        self.ids.lbl_tshirt.text = 'T-Shirt Size: {}'.format(row[10])
        self.ids.lbl_category.text = 'Category: {}'.format(row[16])
        self.ids.lbl_tickettype.text = 'Ticket Type: {}'.format(row[6])
        # Check and display if record is registered?
        self._check_registeration(row[15])

    def _check_registeration(self, reg_no):
        self.ids.but_swag.source = 'atlas://data/default/close'
        self.ids.but_registered.source = 'atlas://data/default/close'
        self.ids.but_tshirt.source = 'atlas://data/default/close'

        # check if file exists
        fname = self.data_file_dir + '/final_registerations.json'
        if not os.path.isfile(fname):
            return

        with open(fname, 'rb') as fn:
            data = fn.read()
            if not data:
                return
            jdata = json.loads(data)
            reg_data = jdata.get(reg_no, None)
            if not reg_data:
                return
            # record exists, update registeration details now
            if 'registered' in reg_data:
                self.ids.but_registered.source = 'atlas://data/default/' +\
                    ('tick' if reg_data['registered'] else 'close')
            if 'swag' in reg_data:
                self.ids.but_swag.source = 'atlas://data/default/' +\
                    ('tick' if reg_data['swag'] else 'close')
            if 'tshirt' in reg_data:
                self.ids.but_tshirt.source = 'atlas://data/default/' +\
                    ('tick' if reg_data['tshirt'] else 'close')

    def _register(self, but, data):
        row = self._row
        if not row:
            return
        if but.source.endswith('tick'):
            return

        but.source = 'atlas://data/default/tick'
        fname = self.data_file_dir + '/final_registerations.json'
        jdata = {}
        r5 = row[15]
        with open(fname, 'rb+' if os.path.isfile(fname) else 'wb+') as fn:
            try:
                jdata = json.load(fn)
            except ValueError:
                pass
            if not jdata.get(r5, None):
                jdata[r5] = {}
            jdata[r5][data] = True
        with open(fname, 'wb') as fn:
            json.dump(jdata, fn)

    def register_user(self, but):
        self._register(but, 'registered')

    def distribute_swag(self, but):
        self._register(but, 'swag')

    def distribute_tshirt(self, but):
        self._register(but, 'tshirt')
