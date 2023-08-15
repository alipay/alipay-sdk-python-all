#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseResourcepackageConsultModel(object):

    def __init__(self):
        self._quantity = None
        self._spec_code = None
        self._time_unit = None

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def spec_code(self):
        return self._spec_code

    @spec_code.setter
    def spec_code(self, value):
        self._spec_code = value
    @property
    def time_unit(self):
        return self._time_unit

    @time_unit.setter
    def time_unit(self, value):
        self._time_unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.spec_code:
            if hasattr(self.spec_code, 'to_alipay_dict'):
                params['spec_code'] = self.spec_code.to_alipay_dict()
            else:
                params['spec_code'] = self.spec_code
        if self.time_unit:
            if hasattr(self.time_unit, 'to_alipay_dict'):
                params['time_unit'] = self.time_unit.to_alipay_dict()
            else:
                params['time_unit'] = self.time_unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseResourcepackageConsultModel()
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'spec_code' in d:
            o.spec_code = d['spec_code']
        if 'time_unit' in d:
            o.time_unit = d['time_unit']
        return o


