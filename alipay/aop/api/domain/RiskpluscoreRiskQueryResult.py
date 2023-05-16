#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RiskpluscoreRiskQueryResult(object):

    def __init__(self):
        self._info_code = None
        self._risk_desc = None
        self._risk_type = None
        self._risk_value = None

    @property
    def info_code(self):
        return self._info_code

    @info_code.setter
    def info_code(self, value):
        self._info_code = value
    @property
    def risk_desc(self):
        return self._risk_desc

    @risk_desc.setter
    def risk_desc(self, value):
        self._risk_desc = value
    @property
    def risk_type(self):
        return self._risk_type

    @risk_type.setter
    def risk_type(self, value):
        self._risk_type = value
    @property
    def risk_value(self):
        return self._risk_value

    @risk_value.setter
    def risk_value(self, value):
        self._risk_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.info_code:
            if hasattr(self.info_code, 'to_alipay_dict'):
                params['info_code'] = self.info_code.to_alipay_dict()
            else:
                params['info_code'] = self.info_code
        if self.risk_desc:
            if hasattr(self.risk_desc, 'to_alipay_dict'):
                params['risk_desc'] = self.risk_desc.to_alipay_dict()
            else:
                params['risk_desc'] = self.risk_desc
        if self.risk_type:
            if hasattr(self.risk_type, 'to_alipay_dict'):
                params['risk_type'] = self.risk_type.to_alipay_dict()
            else:
                params['risk_type'] = self.risk_type
        if self.risk_value:
            if hasattr(self.risk_value, 'to_alipay_dict'):
                params['risk_value'] = self.risk_value.to_alipay_dict()
            else:
                params['risk_value'] = self.risk_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RiskpluscoreRiskQueryResult()
        if 'info_code' in d:
            o.info_code = d['info_code']
        if 'risk_desc' in d:
            o.risk_desc = d['risk_desc']
        if 'risk_type' in d:
            o.risk_type = d['risk_type']
        if 'risk_value' in d:
            o.risk_value = d['risk_value']
        return o


