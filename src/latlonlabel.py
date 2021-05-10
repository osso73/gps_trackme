#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 20:27:01 2021

@author: oriol
"""


# std libraries

# non-std libraries
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, NumericProperty
from kivy.lang import Builder

# my app imports
from constants import *



Builder.load_string(
    r"""

<LatLonLabel>:
    text: "Lat: " + self.lat_label + "\nLon: " + self.lon_label
    size_hint_y: None
    height: self.texture_size[1]
    halign: 'center'
    font_style: 'H5'
    padding: 0, '15dp'

""")



class LatLonLabel(MDLabel):
    """
    Control the label showing the coordinates. If GPS is switched off, it
    shows specific message to indicate it's off.
    
    Attributes
    ----------
    lat : NumericProperty
        Latitude in degrees. This is the attribute updated by GPS. It has two
        special values: NO_GPS_NUM (when GPS is off) and SEARCHING_GPS_NUM,
        after switching GPS and still searching.
    lon : NumericProperty
        Longitude in degrees. Same special values as lat.
    lat_label : StringProperty
        Text to show as latitude.
    lon_label : StringProperty
        Text to show as longitude.
    fmt : string
        Format to show coordinates: 'deg' for decimal degrees, 'dms' for 
        degrees-minutes-seconds.
    
    
    """
    
    lat = NumericProperty(SEARCHING_GPS_NUM)
    lon = NumericProperty(SEARCHING_GPS_NUM)
    lat_label = StringProperty(SEARCHING_GPS_TEXT)
    lon_label = StringProperty(SEARCHING_GPS_TEXT)
    fmt = 'dms'


    def on_lat(self, *args):
        """
        When lat changes, update lat_label.
        """
        
        self.lat_label = self.get_coordinate('lat')
    

    def on_lon(self, *args):
        """
        When lon changes, update lon_label.
        """
        
        self.lon_label = self.get_coordinate('lon')
    

    def on_touch_down(self, touch):
        """
        When label is clicked, change the format of coordinats, and update
        the label with new coordinates.
        
        Parameters
        ----------
        touch : Kicy Touch object
            Contains information about the touch (e.g. coordinates, etc.)

        Returns
        -------
        Boolean
            True to stop searching touch on other objects.
       
        """
        
        if self.collide_point(*touch.pos):
            self.fmt = 'deg' if self.fmt == 'dms' else 'dms'
            self.lat_label = self.get_coordinate('lat')
            self.lon_label = self.get_coordinate('lon')
            return True
    
    

    def get_coordinate(self, coord_type):
        """
        Return the coordinate in text, based on the value of lat/lon. Will
        use self.fmt to format the text.

        Parameters
        ----------
        coord_type : string
            Can be 'lat' for latitude, or 'lon' for longitude.

        Returns
        -------
        string
            Text formatted.

        """
        
        coord = self.lat if coord_type == 'lat' else self.lon

        # special values of coordinate
        if coord == NO_GPS_NUM:
            return NO_GPS_TEXT
        
        if coord == SEARCHING_GPS_NUM:
            return SEARCHING_GPS_TEXT
        
        if self.fmt == 'deg':
            return f'{coord:0.5f}'
        
        else:    # transform to other coordinates
            if coord_type == 'lat':
                letter = 'S' if coord < 0 else 'N'
            else:
                letter = 'W' if coord < 0 else 'E'

            coord = abs(coord)
            d = int(coord)
            rest = (coord - d) * 60
            m = int(rest)
            s = (rest - m) * 60
            
            return f'{letter} {d}º {m}\' {s:.2f}"'
            
    