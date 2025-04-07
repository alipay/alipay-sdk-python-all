#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentRiskProVO(object):

    def __init__(self):
        self._desc = None
        self._risk_level = None
        self._risk_level_type = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def risk_level(self):
        return self._risk_level

    @risk_level.setter
    def risk_level(self, value):
        self._risk_level = value
    @property
    def risk_level_type(self):
        return self._risk_level_type

    @risk_level_type.setter
    def risk_level_type(self, value):
        self._risk_level_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.risk_level:
            if hasattr(self.risk_level, 'to_alipay_dict'):
                params['risk_level'] = self.risk_level.to_alipay_dict()
            else:
                params['risk_level'] = self.risk_level
        if self.risk_level_type:
            if hasattr(self.risk_level_type, 'to_alipay_dict'):
                params['risk_level_type'] = self.risk_level_type.to_alipay_dict()
            else:
                params['risk_level_type'] = self.risk_level_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentRiskProVO()
        if 'desc' in d:
            o.desc = d['desc']
        if 'risk_level' in d:
            o.risk_level = d['risk_level']
        if 'risk_level_type' in d:
            o.risk_level_type = d['risk_level_type']
        return o


