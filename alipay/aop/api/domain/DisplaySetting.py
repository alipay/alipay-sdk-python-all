#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DisplaySetting(object):

    def __init__(self):
        self._color = None
        self._display_text = None
        self._main_tail = None

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
    @property
    def display_text(self):
        return self._display_text

    @display_text.setter
    def display_text(self, value):
        self._display_text = value
    @property
    def main_tail(self):
        return self._main_tail

    @main_tail.setter
    def main_tail(self, value):
        self._main_tail = value


    def to_alipay_dict(self):
        params = dict()
        if self.color:
            if hasattr(self.color, 'to_alipay_dict'):
                params['color'] = self.color.to_alipay_dict()
            else:
                params['color'] = self.color
        if self.display_text:
            if hasattr(self.display_text, 'to_alipay_dict'):
                params['display_text'] = self.display_text.to_alipay_dict()
            else:
                params['display_text'] = self.display_text
        if self.main_tail:
            if hasattr(self.main_tail, 'to_alipay_dict'):
                params['main_tail'] = self.main_tail.to_alipay_dict()
            else:
                params['main_tail'] = self.main_tail
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DisplaySetting()
        if 'color' in d:
            o.color = d['color']
        if 'display_text' in d:
            o.display_text = d['display_text']
        if 'main_tail' in d:
            o.main_tail = d['main_tail']
        return o


