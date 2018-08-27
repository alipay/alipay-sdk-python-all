#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SkuPropertyValue(object):

    def __init__(self):
        self._out_pv_id = None
        self._value = None

    @property
    def out_pv_id(self):
        return self._out_pv_id

    @out_pv_id.setter
    def out_pv_id(self, value):
        self._out_pv_id = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_pv_id:
            if hasattr(self.out_pv_id, 'to_alipay_dict'):
                params['out_pv_id'] = self.out_pv_id.to_alipay_dict()
            else:
                params['out_pv_id'] = self.out_pv_id
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
        o = SkuPropertyValue()
        if 'out_pv_id' in d:
            o.out_pv_id = d['out_pv_id']
        if 'value' in d:
            o.value = d['value']
        return o


