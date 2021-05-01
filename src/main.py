#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 07:52:02 2021

@author: osso73
"""

# std libraries

# non-std libraries
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.settings import SettingsWithSpinner
from kivy.utils import platform

# my app imports
from topbar import TopBar
from latlonlabel import LatLonLabel
from gpshelper import GpsHelper



class MainApp(MDApp):
    
    def on_start(self):
        self.theme_cls.primary_palette = 'DeepOrange'
        self.settings_cls = SettingsWithSpinner
        GpsHelper().run()



if __name__ == '__main__':
    if platform != 'android':
        Window.size = (500, 900)
    
    MainApp().run()

