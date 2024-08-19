#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class JoinPanelInfo(object):

    def __init__(self):
        self._button_text = None
        self._color = None
        self._extra_text = None
        self._side = None

    @property
    def button_text(self):
        return self._button_text

    @button_text.setter
    def button_text(self, value):
        self._button_text = value
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
    @property
    def extra_text(self):
        return self._extra_text

    @extra_text.setter
    def extra_text(self, value):
        self._extra_text = value
    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if isinstance(value, list):
            self._side = list()
            for i in value:
                self._side.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.button_text:
            if hasattr(self.button_text, 'to_alipay_dict'):
                params['button_text'] = self.button_text.to_alipay_dict()
            else:
                params['button_text'] = self.button_text
        if self.color:
            if hasattr(self.color, 'to_alipay_dict'):
                params['color'] = self.color.to_alipay_dict()
            else:
                params['color'] = self.color
        if self.extra_text:
            if hasattr(self.extra_text, 'to_alipay_dict'):
                params['extra_text'] = self.extra_text.to_alipay_dict()
            else:
                params['extra_text'] = self.extra_text
        if self.side:
            if isinstance(self.side, list):
                for i in range(0, len(self.side)):
                    element = self.side[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.side[i] = element.to_alipay_dict()
            if hasattr(self.side, 'to_alipay_dict'):
                params['side'] = self.side.to_alipay_dict()
            else:
                params['side'] = self.side
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JoinPanelInfo()
        if 'button_text' in d:
            o.button_text = d['button_text']
        if 'color' in d:
            o.color = d['color']
        if 'extra_text' in d:
            o.extra_text = d['extra_text']
        if 'side' in d:
            o.side = d['side']
        return o


