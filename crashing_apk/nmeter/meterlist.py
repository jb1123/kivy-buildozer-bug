from kivy.app import App
from kivy.uix.screenmanager import Screen


class MeterList(Screen):
    pass


    def take_picture(self):
        # take picture of meter, it will be used to document readoud
        sm = App.get_running_app().root
        sm.current = 'picture_crop'