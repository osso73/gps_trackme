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
from kivy.lang import Builder

# my app imports
from topbar import TopBar
from latlonlabel import LatLonLabel
from gpshelper import GpsHelper
from mymap import Map
from constants import VERSION


__version__ = VERSION


KV = r"""

Screen:

    BoxLayout:
        orientation: 'vertical'

        TopBar:
            id: topbar
        
        LatLonLabel:
            id: label

        Map:
            id: mapview

"""

class MainApp(MDApp):
    """Main app"""
    
    def build(self):
        """Load KV string"""
        
        screen = Builder.load_string(KV)
        return screen
    
    
    def on_start(self):
        """Set the theme colour, and settings, and start GPS"""
        
        self.theme_cls.primary_palette = 'DeepOrange'
        self.settings_cls = SettingsWithSpinner
        GpsHelper().run()



if __name__ == '__main__':
    if platform != 'android':
        Window.size = (400, 750)
    
    MainApp().run()

