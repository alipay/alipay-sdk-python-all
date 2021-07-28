#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TemplateKeyword(object):

    def __init__(self):
        self._color = None
        self._value = None

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.color:
            if hasattr(self.color, 'to_alipay_dict'):
                params['color'] = self.color.to_alipay_dict()
            else:
                params['color'] = self.color
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TemplateKeyword()
        if 'color' in d:
            o.color = d['color']
        if 'value' in d:
            o.value = d['value']
        return o


