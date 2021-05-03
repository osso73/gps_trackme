#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 17:51:41 2021

@author: oriol
"""

from kivy_garden.mapview import MapView
from kivy.properties import BooleanProperty


class Map(MapView):
    center_map = BooleanProperty(True)
