#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 17:57:34 2021

@author: oriol
"""

from kivy_garden.mapview import MapMarker
from kivy.animation import Animation


class GpsBlinker(MapMarker):
    blinking = False
    
    def _blink(self):
        # Animation that changes the blink size and opacity
        anim = Animation(outer_opacity=0, blink_size=50)
        # When the animation completes, reset the animation, then repeat
        anim.bind(on_complete=self._reset)
        anim.start(self)


    def _reset(self, *args):
        self.outer_opacity = 1
        self.blink_size = self.default_blink_size
        if self.blinking:
            self._blink()

    def stop_blink(self):
        self.blinking = False
        
    
    def start_blink(self):
        self.blinking = True
        self._blink()