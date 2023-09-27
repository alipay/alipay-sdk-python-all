#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAittestOpenapiQueryModel(object):

    def __init__(self):
        self._ait_test_demo = None
        self._ait_test_field = None
        self._ait_test_value = None

    @property
    def ait_test_demo(self):
        return self._ait_test_demo

    @ait_test_demo.setter
    def ait_test_demo(self, value):
        self._ait_test_demo = value
    @property
    def ait_test_field(self):
        return self._ait_test_field

    @ait_test_field.setter
    def ait_test_field(self, value):
        self._ait_test_field = value
    @property
    def ait_test_value(self):
        return self._ait_test_value

    @ait_test_value.setter
    def ait_test_value(self, value):
        self._ait_test_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.ait_test_demo:
            if hasattr(self.ait_test_demo, 'to_alipay_dict'):
                params['ait_test_demo'] = self.ait_test_demo.to_alipay_dict()
            else:
                params['ait_test_demo'] = self.ait_test_demo
        if self.ait_test_field:
            if hasattr(self.ait_test_field, 'to_alipay_dict'):
                params['ait_test_field'] = self.ait_test_field.to_alipay_dict()
            else:
                params['ait_test_field'] = self.ait_test_field
        if self.ait_test_value:
            if hasattr(self.ait_test_value, 'to_alipay_dict'):
                params['ait_test_value'] = self.ait_test_value.to_alipay_dict()
            else:
                params['ait_test_value'] = self.ait_test_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAittestOpenapiQueryModel()
        if 'ait_test_demo' in d:
            o.ait_test_demo = d['ait_test_demo']
        if 'ait_test_field' in d:
            o.ait_test_field = d['ait_test_field']
        if 'ait_test_value' in d:
            o.ait_test_value = d['ait_test_value']
        return o


