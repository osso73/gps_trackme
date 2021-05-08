#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 22:13:43 2021

@author: oriol
"""

# std libraries


# non-std libraries
from kivy.properties import StringProperty
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDFlatButton
from kivymd.uix.list import OneLineIconListItem, ThreeLineIconListItem
from kivymd.uix.dialog import MDDialog


# my app imports
from constants import *


Builder.load_string(
    '''
<MenuItem>:
    IconLeftWidget:
        icon: root.icon


<LogItem>:
    IconLeftWidget:
        icon: 'map-marker-check'
''')



class Menu(MDDropdownMenu):
    def see_log(self, *args):
        def close_log(button):
            log_view.dismiss()
        
        def clear_log(button):
            with open(LOG_FILE, 'wt') as f:
                pass  # create empty file
            log_view.dismiss()
        
        self.dismiss()
        try:
            with open(LOG_FILE) as f:
                lines = f.readlines()
        except FileNotFoundError:
            lines = []
        
        items_list = []
        for line in lines:
            lat, lon, timestamp, comment = line[:-1].split(';')
            date, time = timestamp.split('T')
            element = LogItem(
                text=lat + " " + lon,
                secondary_text=f'On {date} at {time}',
                tertiary_text=comment)
            items_list.append(element)
        
        
        log_view = MDDialog(title='Log view',
                            type='confirmation',
                            items=items_list,
                            size_hint_x=0.9,
                            buttons=[
                                MDFlatButton(text='CLEAR',
                                             on_release=clear_log),
                                MDFlatButton(text='CLOSE',
                                             on_release=close_log)
                                ]
                            )
        log_view.open()
        

    
    def about(self, *args):
        print('about', args)
        self.dismiss()
    
    def help(self):
        print('help')
        self.dismiss()
    
    def settings(self):
        print('settings')
        app = MDApp.get_running_app()
        app.open_settings()
        self.dismiss()
    
    
    def create_menu(self, caller):
        self.items = [
            {'viewclass': 'MenuItem',
             'icon': 'view-list',
             'text': 'See log',
             'on_release': self.see_log
             },
            {'viewclass': 'MenuItem',
             'icon': 'language-python',
             'text': 'About',
             'on_release': self.about
             },
            {'viewclass': 'MenuItem',
             'icon': 'help',
             'text': 'Help',
             'on_release': self.help
             },
            {'viewclass': 'MenuItem',
             'icon': 'language-python',
             'text': 'Settings',
             'on_release': self.settings
             }
            ]
        
        self.caller = caller
        self.width_mult=4

        return self
        

class MenuItem(OneLineIconListItem):
    icon = StringProperty()


class LogItem(ThreeLineIconListItem):
    pass
