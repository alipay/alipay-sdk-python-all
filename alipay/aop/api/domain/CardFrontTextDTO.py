#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CardFrontTextDTO(object):

    def __init__(self):
        self._label = None
        self._value = None

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        self._label = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.label:
            if hasattr(self.label, 'to_alipay_dict'):
                params['label'] = self.label.to_alipay_dict()
            else:
                params['label'] = self.label
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
        o = CardFrontTextDTO()
        if 'label' in d:
            o.label = d['label']
        if 'value' in d:
            o.value = d['value']
        return o


