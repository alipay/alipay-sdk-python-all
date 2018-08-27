# -*- coding: utf-8 -*-
'''
Created on 2017-12-20

@author: liuqun
'''


def add_start_end(key, startMarker, endMarker):
    if key.find(startMarker) < 0:
        key = startMarker + key
    if key.find(endMarker) < 0:
        key = key + endMarker
    return key
