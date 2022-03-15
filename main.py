# -*- coding: utf-8 -*-

import ui
import photos
import dialogs
import console
from objc_util import ObjCInstance, on_main_thread

import math
import json
import os
import time
import sys

from .modules.vent.compairstring import compairString
from .modules.vent.ease import Ease

# ui items function

def on_button_delete():
    pass

# init process

def awake():
    pass

def start():
    pass

# main

if __name__ == '__main__':
    global v
    
    v = ui.load_view()
    awake()
            
    v.present('fullscreen')
    start()