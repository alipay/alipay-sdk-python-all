#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantScreenHit(object):

    def __init__(self):
        self._input_type = None
        self._risk_detail = None

    @property
    def input_type(self):
        return self._input_type

    @input_type.setter
    def input_type(self, value):
        self._input_type = value
    @property
    def risk_detail(self):
        return self._risk_detail

    @risk_detail.setter
    def risk_detail(self, value):
        self._risk_detail = value


    def to_alipay_dict(self):
        params = dict()
        if self.input_type:
            if hasattr(self.input_type, 'to_alipay_dict'):
                params['input_type'] = self.input_type.to_alipay_dict()
            else:
                params['input_type'] = self.input_type
        if self.risk_detail:
            if hasattr(self.risk_detail, 'to_alipay_dict'):
                params['risk_detail'] = self.risk_detail.to_alipay_dict()
            else:
                params['risk_detail'] = self.risk_detail
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantScreenHit()
        if 'input_type' in d:
            o.input_type = d['input_type']
        if 'risk_detail' in d:
            o.risk_detail = d['risk_detail']
        return o


