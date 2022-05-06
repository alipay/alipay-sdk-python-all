#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnswerDTO(object):

    def __init__(self):
        self._initial_value = None
        self._label_name = None
        self._value = None

    @property
    def initial_value(self):
        return self._initial_value

    @initial_value.setter
    def initial_value(self, value):
        self._initial_value = value
    @property
    def label_name(self):
        return self._label_name

    @label_name.setter
    def label_name(self, value):
        self._label_name = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.initial_value:
            if hasattr(self.initial_value, 'to_alipay_dict'):
                params['initial_value'] = self.initial_value.to_alipay_dict()
            else:
                params['initial_value'] = self.initial_value
        if self.label_name:
            if hasattr(self.label_name, 'to_alipay_dict'):
                params['label_name'] = self.label_name.to_alipay_dict()
            else:
                params['label_name'] = self.label_name
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
        o = AnswerDTO()
        if 'initial_value' in d:
            o.initial_value = d['initial_value']
        if 'label_name' in d:
            o.label_name = d['label_name']
        if 'value' in d:
            o.value = d['value']
        return o


