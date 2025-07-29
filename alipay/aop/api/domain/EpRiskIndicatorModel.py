#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpRiskIndicatorModel(object):

    def __init__(self):
        self._label_code = None
        self._label_name = None
        self._label_value = None

    @property
    def label_code(self):
        return self._label_code

    @label_code.setter
    def label_code(self, value):
        self._label_code = value
    @property
    def label_name(self):
        return self._label_name

    @label_name.setter
    def label_name(self, value):
        self._label_name = value
    @property
    def label_value(self):
        return self._label_value

    @label_value.setter
    def label_value(self, value):
        self._label_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.label_code:
            if hasattr(self.label_code, 'to_alipay_dict'):
                params['label_code'] = self.label_code.to_alipay_dict()
            else:
                params['label_code'] = self.label_code
        if self.label_name:
            if hasattr(self.label_name, 'to_alipay_dict'):
                params['label_name'] = self.label_name.to_alipay_dict()
            else:
                params['label_name'] = self.label_name
        if self.label_value:
            if hasattr(self.label_value, 'to_alipay_dict'):
                params['label_value'] = self.label_value.to_alipay_dict()
            else:
                params['label_value'] = self.label_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpRiskIndicatorModel()
        if 'label_code' in d:
            o.label_code = d['label_code']
        if 'label_name' in d:
            o.label_name = d['label_name']
        if 'label_value' in d:
            o.label_value = d['label_value']
        return o


