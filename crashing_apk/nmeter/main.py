import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

from meterlist import MeterList
from picturecrop import PictureCrop
from readmeter import ReadMeter


class ImageButton(Button):
    """
    To be converted to (buttonbehaviour, Image)
    """
    pass

class MetereadApp(App):

    def build(self):
        sm = ScreenManager()
        Builder.load_file('gui_layout.kv')
        sm.add_widget(MeterList())
        sm.add_widget(PictureCrop())
        sm.add_widget(ReadMeter())
        sm.current = 'meter_list'
        self.manager = sm
        return sm


if __name__ == '__main__':
    MetereadApp().run()