#!/usr/bin/env python3

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

import datetime

class UebersichtScreen(Screen):
    pass

class MainScreen(Screen):

    def currentTime(self):
        



class Manager(ScreenManager):
    main_screen = ObjectProperty(None)
    uebersicht_screen = ObjectProperty(None)


class ZeiterfassungApp(App):
    def __init__(self, **kwargs):
        super(ZeiterfassungApp, self).__init__(**kwargs)

    def build(self):
        return Manager()

if __name__ == '__main__':
    ZeiterfassungApp().run()
