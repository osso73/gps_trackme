#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 20:02:38 2021

@author: oriol
"""

# std libraries
import datetime as dt

# non-std libraries
from kivy.properties import StringProperty, NumericProperty, ObjectProperty

from kivymd.uix.toolbar import MDToolbar
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField

# my app imports
from gpshelper import GpsHelper
from menu import Menu
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
    accuracy : NumericProperty
        Keeps the level of accuracy, as reported by GPS system. This enables
        to show the right icon for accuracy.
    menu : MDMenuDropDown
        Contains the dropdown menu that will open when clicking the icon.
    '''
    icon_gps = StringProperty('crosshairs')
    icon_accuracy = StringProperty('signal-cellular-outline')
    gps_status = StringProperty('searching')
    accuracy = NumericProperty(-1)
    
    def btn_menu(self, *args):
        if not hasattr(self, 'menu'):
            self.menu = Menu().create_menu(self.ids.menu)
        self.menu.open()


    def btn_track(self, *args):
        
        def cancel(button):
            msg.dismiss()
        
        def save_log(button):
            now = dt.datetime.now()
            timestamp = now.isoformat(timespec='seconds')
            
            app = MDApp.get_running_app()
            label = app.root.ids.label
            lat = label.get_coordinate('lat')
            lon = label.get_coordinate('lon')
            
            comment = msg.content_cls.text
    
            line = ";".join([lat, lon, timestamp, comment])+'\n'
            with open(LOG_FILE, 'at') as f:
                f.write(line)
            
            msg.dismiss()

        msg = MDDialog(type='custom',
                  title='Comment',
                  content_cls=MDTextField(
                      hint_text='Enter a comment',
                      helper_text='to be saved with your location',
                      helper_text_mode='on_focus',
                      on_text_validate=save_log
                      ),
                  buttons=[
                      MDFlatButton(text="SAVE", on_release=save_log),
                      MDFlatButton(text="CANCEL", on_release=cancel),
                      ]
                  )
        msg.open()
    
    def btn_gps(self, *args):
        if self.gps_status == 'off':
            GpsHelper().run()
            self.gps_status = 'searching'

        else:
            GpsHelper().stop()
            self.gps_status = 'off'


    def on_gps_status(self, *args):
        app = MDApp.get_running_app()
        label = app.root.ids.label
        gps_blinker = app.root.ids.mapview.ids.blinker

        if self.gps_status == 'on':
            self.icon_gps = 'crosshairs-gps'
            gps_blinker.start_blink()

        elif self.gps_status == 'searching':
            self.icon_gps = 'crosshairs'
            label.lat = label.lon = SEARCHING_GPS_NUM
            gps_blinker.stop_blink()

        else:
            self.icon_gps = 'crosshairs-off'
            self.accuracy = -1
            label.lat = label.lon = NO_GPS_NUM
            gps_blinker.stop_blink()
    
    
    def on_accuracy(self, *args):
        if self.accuracy == -1:
            self.icon_accuracy = 'signal-cellular-outline'
        elif self.accuracy <= 6:
            self.icon_accuracy = 'signal-cellular-3'
        elif self.accuracy <= 20:
            self.icon_accuracy = 'signal-cellular-2'
        else:
            self.icon_accuracy = 'signal-cellular-1'


class ToolbarIcon(MDIconButton):
    pass

