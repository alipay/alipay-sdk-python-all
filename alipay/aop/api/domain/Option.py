#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Option(object):

    def __init__(self):
        self._text = None
        self._value = None

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
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
        o = Option()
        if 'text' in d:
            o.text = d['text']
        if 'value' in d:
            o.value = d['value']
        return o


