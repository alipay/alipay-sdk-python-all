#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RiskProfileDto(object):

    def __init__(self):
        self._risk_profile = None
        self._value = None

    @property
    def risk_profile(self):
        return self._risk_profile

    @risk_profile.setter
    def risk_profile(self, value):
        self._risk_profile = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.risk_profile:
            if hasattr(self.risk_profile, 'to_alipay_dict'):
                params['risk_profile'] = self.risk_profile.to_alipay_dict()
            else:
                params['risk_profile'] = self.risk_profile
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
        o = RiskProfileDto()
        if 'risk_profile' in d:
            o.risk_profile = d['risk_profile']
        if 'value' in d:
            o.value = d['value']
        return o


