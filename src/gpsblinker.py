#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 17:57:34 2021

@author: oriol
"""

# std libraries

# non-std libraries
from kivy_garden.mapview import MapMarker
from kivy.animation import Animation
from kivy.lang import Builder

# my app imports




Builder.load_string(
    r"""

<GpsBlinker>:
    default_blink_size: 25
    blink_size: 25
    source: 'images/transparent.png'
    outer_opacity: 1

    canvas.before:
        # Outer circle
        Color:
            rgba: app.theme_cls.primary_color[:3] + [root.outer_opacity]
        RoundedRectangle:
            radius: [root.blink_size/2.0, ]
            size: [root.blink_size, root.blink_size]
            pos: root.pos[0] + root.size[0]/2.0 - root.blink_size/2.0, root.pos[1] + root.size[1]/2.0 - root.blink_size/2.0

        # Inner Circle
        Color:
            rgba: app.theme_cls.primary_color
        RoundedRectangle:
            radius: [root.default_blink_size/2.0, ]
            size: [root.default_blink_size, root.default_blink_size]
            pos: [root.pos[0] + root.size[0]/2.0 - root.default_blink_size/2.0, root.pos[1] + root.size[1]/2.0 - root.default_blink_size/2.0]

""")



class GpsBlinker(MapMarker):
    """
    Create a blinking cursor to show the GPS position on the map.
    
    Attributes
    ----------
    blinking : bool
        Defines whether the blinker should be blinking or not. If False,
        blinking stops.
    
    """
    
    blinking = False
    
    def _blink(self):
        """
        Start the animation of blinking: outer circle grows larger, and
        its opacity decreases.
        """
        
        # Animation that changes the blink size and opacity
        anim = Animation(outer_opacity=0, blink_size=100)
        
        # When the animation completes, reset the animation, then repeat
        anim.bind(on_complete=self._reset)
        anim.start(self)


    def _reset(self, *args):
        """
        Reset the parameters to its default values, and relaunch animation.
        If blinking is False, it will not relaunch, so the blinking will
        stop.
        """
        
        self.outer_opacity = 1
        self.blink_size = self.default_blink_size
        if self.blinking:
            self._blink()


    def stop_blink(self):
        """
        Method to stop blinking.
        """
        
        self.blinking = False
        
    
    def start_blink(self):
        """
        Method to start blinking. Use this, rather than _blink(), to ensure
        reset of the blinking attribute.
        """
        
        self.blinking = True
        self._blink()