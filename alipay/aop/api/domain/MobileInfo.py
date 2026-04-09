#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MobileInfo(object):

    def __init__(self):
        self._carrier = None
        self._province = None
        self._sub_operator = None

    @property
    def carrier(self):
        return self._carrier

    @carrier.setter
    def carrier(self, value):
        self._carrier = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def sub_operator(self):
        return self._sub_operator

    @sub_operator.setter
    def sub_operator(self, value):
        self._sub_operator = value


    def to_alipay_dict(self):
        params = dict()
        if self.carrier:
            if hasattr(self.carrier, 'to_alipay_dict'):
                params['carrier'] = self.carrier.to_alipay_dict()
            else:
                params['carrier'] = self.carrier
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.sub_operator:
            if hasattr(self.sub_operator, 'to_alipay_dict'):
                params['sub_operator'] = self.sub_operator.to_alipay_dict()
            else:
                params['sub_operator'] = self.sub_operator
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MobileInfo()
        if 'carrier' in d:
            o.carrier = d['carrier']
        if 'province' in d:
            o.province = d['province']
        if 'sub_operator' in d:
            o.sub_operator = d['sub_operator']
        return o


