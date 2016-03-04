from kivy.factory import Factory
from kivy.properties import StringProperty, ListProperty


class EventItemDetail(Factory.Popup):

    description = StringProperty('')

    image = StringProperty('')