#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NewsfeedMediaImg(object):

    def __init__(self):
        self._height = None
        self._src = None
        self._width = None

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
    @property
    def src(self):
        return self._src

    @src.setter
    def src(self, value):
        self._src = value
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
        if self.src:
            if hasattr(self.src, 'to_alipay_dict'):
                params['src'] = self.src.to_alipay_dict()
            else:
                params['src'] = self.src
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
        o = NewsfeedMediaImg()
        if 'height' in d:
            o.height = d['height']
        if 'src' in d:
            o.src = d['src']
        if 'width' in d:
            o.width = d['width']
        return o


