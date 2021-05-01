#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 20:02:38 2021

@author: oriol
"""

# std libraries

# non-std libraries
from kivymd.uix.toolbar import MDToolbar
from kivymd.app import MDApp
from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.label import MDIcon

# my app imports
from gpshelper import GpsHelper
from constants import *



class TopBar(MDToolbar):
    '''
    Control the toolbar and the buttons.
    
    Attributes
    ----------
    icon_gps : StringProperty
        Icon to display the status of gps. Can be any of: 'crosshairs',
        'crosshairs-gps', 'crosshairs-off'
    icon_accuracy : StringProperty
        icon to display the level of accuracy. Can be any of: 'signal-
        cellular-outline', 'signal-cellular-1', 'signal-cellular-2',
        'signal-cellular-3'.
    gps_status : StringProperty
        Can be 'on', 'off' or 'searching'. This controls the icons and the
        messages to be displayed
    '''
    icon_gps = StringProperty('crosshairs')
    icon_accuracy = StringProperty('signal-cellular-outline')
    gps_status = StringProperty('on')


    def open_menu(self, *args):
        pass


    def track_route(self, *args):
        pass


    def capture_location(self, *args):
        pass
    
    
    def on_gps_status(self, *args):
        app = MDApp.get_running_app()
        label = app.root.ids.label

        if self.gps_status == 'on':
            self.icon_gps = 'crosshairs-gps'

        elif self.gps_status == 'searching':
            self.icon_gps = 'crosshairs'
            label.lat = label.lon = SEARCHING_GPS_NUM

        else:
            self.icon_gps = 'crosshairs-off'
            self.icon_accuracy = 'signal-cellular-outline'
            label.lat = label.lon = NO_GPS_NUM


    def activate_gps(self, *args):
        app = MDApp.get_running_app()

        if self.gps_status == 'off':
            GpsHelper().run()
            self.gps_status = 'searching'

        else:
            GpsHelper().stop()
            self.gps_status = 'off'


    def do_nothing(self, *args):
        pass


class ToolbarIcon(MDIcon):
    callback = ObjectProperty()
    
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.callback()
            return True

        