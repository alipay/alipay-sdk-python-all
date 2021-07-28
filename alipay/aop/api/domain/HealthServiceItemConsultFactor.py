#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HealthServiceItemConsultFactor(object):

    def __init__(self):
        self._factor_key = None
        self._factor_value = None

    @property
    def factor_key(self):
        return self._factor_key

    @factor_key.setter
    def factor_key(self, value):
        self._factor_key = value
    @property
    def factor_value(self):
        return self._factor_value

    @factor_value.setter
    def factor_value(self, value):
        self._factor_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.factor_key:
            if hasattr(self.factor_key, 'to_alipay_dict'):
                params['factor_key'] = self.factor_key.to_alipay_dict()
            else:
                params['factor_key'] = self.factor_key
        if self.factor_value:
            if hasattr(self.factor_value, 'to_alipay_dict'):
                params['factor_value'] = self.factor_value.to_alipay_dict()
            else:
                params['factor_value'] = self.factor_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HealthServiceItemConsultFactor()
        if 'factor_key' in d:
            o.factor_key = d['factor_key']
        if 'factor_value' in d:
            o.factor_value = d['factor_value']
        return o


