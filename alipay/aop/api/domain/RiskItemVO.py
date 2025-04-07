#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RiskItemVO(object):

    def __init__(self):
        self._hit_detail = None
        self._risk_code = None
        self._risk_level = None

    @property
    def hit_detail(self):
        return self._hit_detail

    @hit_detail.setter
    def hit_detail(self, value):
        self._hit_detail = value
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
        if self.hit_detail:
            if hasattr(self.hit_detail, 'to_alipay_dict'):
                params['hit_detail'] = self.hit_detail.to_alipay_dict()
            else:
                params['hit_detail'] = self.hit_detail
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
        if 'hit_detail' in d:
            o.hit_detail = d['hit_detail']
        if 'risk_code' in d:
            o.risk_code = d['risk_code']
        if 'risk_level' in d:
            o.risk_level = d['risk_level']
        return o


