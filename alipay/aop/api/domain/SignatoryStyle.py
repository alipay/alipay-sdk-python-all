#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SignatoryStyle(object):

    def __init__(self):
        self._font = None
        self._font_size = None
        self._height = None
        self._text_color = None
        self._width = None

    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, value):
        self._font = value
    @property
    def font_size(self):
        return self._font_size

    @font_size.setter
    def font_size(self, value):
        self._font_size = value
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
    @property
    def text_color(self):
        return self._text_color

    @text_color.setter
    def text_color(self, value):
        self._text_color = value
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value


    def to_alipay_dict(self):
        params = dict()
        if self.font:
            if hasattr(self.font, 'to_alipay_dict'):
                params['font'] = self.font.to_alipay_dict()
            else:
                params['font'] = self.font
        if self.font_size:
            if hasattr(self.font_size, 'to_alipay_dict'):
                params['font_size'] = self.font_size.to_alipay_dict()
            else:
                params['font_size'] = self.font_size
        if self.height:
            if hasattr(self.height, 'to_alipay_dict'):
                params['height'] = self.height.to_alipay_dict()
            else:
                params['height'] = self.height
        if self.text_color:
            if hasattr(self.text_color, 'to_alipay_dict'):
                params['text_color'] = self.text_color.to_alipay_dict()
            else:
                params['text_color'] = self.text_color
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
        o = SignatoryStyle()
        if 'font' in d:
            o.font = d['font']
        if 'font_size' in d:
            o.font_size = d['font_size']
        if 'height' in d:
            o.height = d['height']
        if 'text_color' in d:
            o.text_color = d['text_color']
        if 'width' in d:
            o.width = d['width']
        return o


