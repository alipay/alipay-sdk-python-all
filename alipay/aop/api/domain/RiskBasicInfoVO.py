#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RiskBasicInfoVO(object):

    def __init__(self):
        self._risk_policy_value = None
        self._risk_scheme_id = None

    @property
    def risk_policy_value(self):
        return self._risk_policy_value

    @risk_policy_value.setter
    def risk_policy_value(self, value):
        self._risk_policy_value = value
    @property
    def risk_scheme_id(self):
        return self._risk_scheme_id

    @risk_scheme_id.setter
    def risk_scheme_id(self, value):
        self._risk_scheme_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.risk_policy_value:
            if hasattr(self.risk_policy_value, 'to_alipay_dict'):
                params['risk_policy_value'] = self.risk_policy_value.to_alipay_dict()
            else:
                params['risk_policy_value'] = self.risk_policy_value
        if self.risk_scheme_id:
            if hasattr(self.risk_scheme_id, 'to_alipay_dict'):
                params['risk_scheme_id'] = self.risk_scheme_id.to_alipay_dict()
            else:
                params['risk_scheme_id'] = self.risk_scheme_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RiskBasicInfoVO()
        if 'risk_policy_value' in d:
            o.risk_policy_value = d['risk_policy_value']
        if 'risk_scheme_id' in d:
            o.risk_scheme_id = d['risk_scheme_id']
        return o


