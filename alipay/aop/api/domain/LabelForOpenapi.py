#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LabelForOpenapi(object):

    def __init__(self):
        self._label_type = None
        self._value = None

    @property
    def label_type(self):
        return self._label_type

    @label_type.setter
    def label_type(self, value):
        self._label_type = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.label_type:
            if hasattr(self.label_type, 'to_alipay_dict'):
                params['label_type'] = self.label_type.to_alipay_dict()
            else:
                params['label_type'] = self.label_type
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
        o = LabelForOpenapi()
        if 'label_type' in d:
            o.label_type = d['label_type']
        if 'value' in d:
            o.value = d['value']
        return o


