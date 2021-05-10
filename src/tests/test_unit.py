#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 07:52:36 2021

@author: osso73
"""

import pytest
import sys
import os

from topbar import TopBar

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestTopBar():
    def test_fake(self):
        assert True