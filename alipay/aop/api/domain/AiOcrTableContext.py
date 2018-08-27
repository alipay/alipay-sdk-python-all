#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AiOcrTableContext(object):

    def __init__(self):
        self._ex = None
        self._ey = None
        self._height = None
        self._sx = None
        self._sy = None
        self._text = None
        self._type = None
        self._width = None

    @property
    def ex(self):
        return self._ex

    @ex.setter
    def ex(self, value):
        self._ex = value
    @property
    def ey(self):
        return self._ey

    @ey.setter
    def ey(self, value):
        self._ey = value
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
    @property
    def sx(self):
        return self._sx

    @sx.setter
    def sx(self, value):
        self._sx = value
    @property
    def sy(self):
        return self._sy

    @sy.setter
    def sy(self, value):
        self._sy = value
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if isinstance(value, list):
            self._text = list()
            for i in value:
                self._text.append(i)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value


    def to_alipay_dict(self):
        params = dict()
        if self.ex:
            if hasattr(self.ex, 'to_alipay_dict'):
                params['ex'] = self.ex.to_alipay_dict()
            else:
                params['ex'] = self.ex
        if self.ey:
            if hasattr(self.ey, 'to_alipay_dict'):
                params['ey'] = self.ey.to_alipay_dict()
            else:
                params['ey'] = self.ey
        if self.height:
            if hasattr(self.height, 'to_alipay_dict'):
                params['height'] = self.height.to_alipay_dict()
            else:
                params['height'] = self.height
        if self.sx:
            if hasattr(self.sx, 'to_alipay_dict'):
                params['sx'] = self.sx.to_alipay_dict()
            else:
                params['sx'] = self.sx
        if self.sy:
            if hasattr(self.sy, 'to_alipay_dict'):
                params['sy'] = self.sy.to_alipay_dict()
            else:
                params['sy'] = self.sy
        if self.text:
            if isinstance(self.text, list):
                for i in range(0, len(self.text)):
                    element = self.text[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.text[i] = element.to_alipay_dict()
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
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
        o = AiOcrTableContext()
        if 'ex' in d:
            o.ex = d['ex']
        if 'ey' in d:
            o.ey = d['ey']
        if 'height' in d:
            o.height = d['height']
        if 'sx' in d:
            o.sx = d['sx']
        if 'sy' in d:
            o.sy = d['sy']
        if 'text' in d:
            o.text = d['text']
        if 'type' in d:
            o.type = d['type']
        if 'width' in d:
            o.width = d['width']
        return o


