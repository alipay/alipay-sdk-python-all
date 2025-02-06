#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RiskItemVO(object):

    def __init__(self):
        self._risk_code = None
        self._risk_level = None

    @property
    def risk_code(self):
        return self._risk_code

    @risk_code.setter
    def risk_code(self, value):
        self._risk_code = value
    @property
    def risk_level(self):
        return self._risk_level

    @risk_level.setter
    def risk_level(self, value):
        self._risk_level = value


    def to_alipay_dict(self):
        params = dict()
        if self.risk_code:
            if hasattr(self.risk_code, 'to_alipay_dict'):
                params['risk_code'] = self.risk_code.to_alipay_dict()
            else:
                params['risk_code'] = self.risk_code
        if self.risk_level:
            if hasattr(self.risk_level, 'to_alipay_dict'):
                params['risk_level'] = self.risk_level.to_alipay_dict()
            else:
                params['risk_level'] = self.risk_level
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RiskItemVO()
        if 'risk_code' in d:
            o.risk_code = d['risk_code']
        if 'risk_level' in d:
            o.risk_level = d['risk_level']
        return o


