#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BreakCostsInfo(object):

    def __init__(self):
        self._damages_rate = None
        self._damages_type = None

    @property
    def damages_rate(self):
        return self._damages_rate

    @damages_rate.setter
    def damages_rate(self, value):
        self._damages_rate = value
    @property
    def damages_type(self):
        return self._damages_type

    @damages_type.setter
    def damages_type(self, value):
        self._damages_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.damages_rate:
            if hasattr(self.damages_rate, 'to_alipay_dict'):
                params['damages_rate'] = self.damages_rate.to_alipay_dict()
            else:
                params['damages_rate'] = self.damages_rate
        if self.damages_type:
            if hasattr(self.damages_type, 'to_alipay_dict'):
                params['damages_type'] = self.damages_type.to_alipay_dict()
            else:
                params['damages_type'] = self.damages_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BreakCostsInfo()
        if 'damages_rate' in d:
            o.damages_rate = d['damages_rate']
        if 'damages_type' in d:
            o.damages_type = d['damages_type']
        return o


