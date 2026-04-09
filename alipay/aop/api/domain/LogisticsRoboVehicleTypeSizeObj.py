#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LogisticsRoboVehicleTypeSizeObj(object):

    def __init__(self):
        self._height = None
        self._length = None
        self._width = None

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value


    def to_alipay_dict(self):
        params = dict()
        if self.height:
            if hasattr(self.height, 'to_alipay_dict'):
                params['height'] = self.height.to_alipay_dict()
            else:
                params['height'] = self.height
        if self.length:
            if hasattr(self.length, 'to_alipay_dict'):
                params['length'] = self.length.to_alipay_dict()
            else:
                params['length'] = self.length
        if self.width:
            if hasattr(self.width, 'to_alipay_dict'):
                params['width'] = self.width.to_alipay_dict()
            else:
                params['width'] = self.width
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LogisticsRoboVehicleTypeSizeObj()
        if 'height' in d:
            o.height = d['height']
        if 'length' in d:
            o.length = d['length']
        if 'width' in d:
            o.width = d['width']
        return o


