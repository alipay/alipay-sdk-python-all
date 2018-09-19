#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InfoCode(object):

    def __init__(self):
        self._risk_description = None
        self._risk_factor_code = None
        self._risk_factor_name = None
        self._risk_magnitude = None

    @property
    def risk_description(self):
        return self._risk_description

    @risk_description.setter
    def risk_description(self, value):
        self._risk_description = value
    @property
    def risk_factor_code(self):
        return self._risk_factor_code

    @risk_factor_code.setter
    def risk_factor_code(self, value):
        self._risk_factor_code = value
    @property
    def risk_factor_name(self):
        return self._risk_factor_name

    @risk_factor_name.setter
    def risk_factor_name(self, value):
        self._risk_factor_name = value
    @property
    def risk_magnitude(self):
        return self._risk_magnitude

    @risk_magnitude.setter
    def risk_magnitude(self, value):
        self._risk_magnitude = value


    def to_alipay_dict(self):
        params = dict()
        if self.risk_description:
            if hasattr(self.risk_description, 'to_alipay_dict'):
                params['risk_description'] = self.risk_description.to_alipay_dict()
            else:
                params['risk_description'] = self.risk_description
        if self.risk_factor_code:
            if hasattr(self.risk_factor_code, 'to_alipay_dict'):
                params['risk_factor_code'] = self.risk_factor_code.to_alipay_dict()
            else:
                params['risk_factor_code'] = self.risk_factor_code
        if self.risk_factor_name:
            if hasattr(self.risk_factor_name, 'to_alipay_dict'):
                params['risk_factor_name'] = self.risk_factor_name.to_alipay_dict()
            else:
                params['risk_factor_name'] = self.risk_factor_name
        if self.risk_magnitude:
            if hasattr(self.risk_magnitude, 'to_alipay_dict'):
                params['risk_magnitude'] = self.risk_magnitude.to_alipay_dict()
            else:
                params['risk_magnitude'] = self.risk_magnitude
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InfoCode()
        if 'risk_description' in d:
            o.risk_description = d['risk_description']
        if 'risk_factor_code' in d:
            o.risk_factor_code = d['risk_factor_code']
        if 'risk_factor_name' in d:
            o.risk_factor_name = d['risk_factor_name']
        if 'risk_magnitude' in d:
            o.risk_magnitude = d['risk_magnitude']
        return o


