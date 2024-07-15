#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ProductProperty(object):

    def __init__(self):
        self._text = None
        self._values = None

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, value):
        if isinstance(value, list):
            self._values = list()
            for i in value:
                self._values.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        if self.values:
            if isinstance(self.values, list):
                for i in range(0, len(self.values)):
                    element = self.values[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.values[i] = element.to_alipay_dict()
            if hasattr(self.values, 'to_alipay_dict'):
                params['values'] = self.values.to_alipay_dict()
            else:
                params['values'] = self.values
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProductProperty()
        if 'text' in d:
            o.text = d['text']
        if 'values' in d:
            o.values = d['values']
        return o


