#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantItemExtParam(object):

    def __init__(self):
        self._param_key = None
        self._param_value = None

    @property
    def param_key(self):
        return self._param_key

    @param_key.setter
    def param_key(self, value):
        self._param_key = value
    @property
    def param_value(self):
        return self._param_value

    @param_value.setter
    def param_value(self, value):
        self._param_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.param_key:
            if hasattr(self.param_key, 'to_alipay_dict'):
                params['param_key'] = self.param_key.to_alipay_dict()
            else:
                params['param_key'] = self.param_key
        if self.param_value:
            if hasattr(self.param_value, 'to_alipay_dict'):
                params['param_value'] = self.param_value.to_alipay_dict()
            else:
                params['param_value'] = self.param_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantItemExtParam()
        if 'param_key' in d:
            o.param_key = d['param_key']
        if 'param_value' in d:
            o.param_value = d['param_value']
        return o


