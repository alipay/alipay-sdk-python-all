#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CheckDetails(object):

    def __init__(self):
        self._new_value = None
        self._value = None

    @property
    def new_value(self):
        return self._new_value

    @new_value.setter
    def new_value(self, value):
        self._new_value = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.new_value:
            if hasattr(self.new_value, 'to_alipay_dict'):
                params['new_value'] = self.new_value.to_alipay_dict()
            else:
                params['new_value'] = self.new_value
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
        o = CheckDetails()
        if 'new_value' in d:
            o.new_value = d['new_value']
        if 'value' in d:
            o.value = d['value']
        return o


