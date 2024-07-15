#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NbDrawSize(object):

    def __init__(self):
        self._height = None
        self._width = None

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
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
        o = NbDrawSize()
        if 'height' in d:
            o.height = d['height']
        if 'width' in d:
            o.width = d['width']
        return o


