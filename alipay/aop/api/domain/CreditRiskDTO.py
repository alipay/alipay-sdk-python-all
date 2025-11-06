#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditRiskDTO(object):

    def __init__(self):
        self._can_retry = None
        self._data = None
        self._risk_code = None

    @property
    def can_retry(self):
        return self._can_retry

    @can_retry.setter
    def can_retry(self, value):
        self._can_retry = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def risk_code(self):
        return self._risk_code

    @risk_code.setter
    def risk_code(self, value):
        self._risk_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.can_retry:
            if hasattr(self.can_retry, 'to_alipay_dict'):
                params['can_retry'] = self.can_retry.to_alipay_dict()
            else:
                params['can_retry'] = self.can_retry
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.risk_code:
            if hasattr(self.risk_code, 'to_alipay_dict'):
                params['risk_code'] = self.risk_code.to_alipay_dict()
            else:
                params['risk_code'] = self.risk_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditRiskDTO()
        if 'can_retry' in d:
            o.can_retry = d['can_retry']
        if 'data' in d:
            o.data = d['data']
        if 'risk_code' in d:
            o.risk_code = d['risk_code']
        return o


