#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditRiskInfo(object):

    def __init__(self):
        self._can_retry = None
        self._code = None
        self._data = None

    @property
    def can_retry(self):
        return self._can_retry

    @can_retry.setter
    def can_retry(self, value):
        self._can_retry = value
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value


    def to_alipay_dict(self):
        params = dict()
        if self.can_retry:
            if hasattr(self.can_retry, 'to_alipay_dict'):
                params['can_retry'] = self.can_retry.to_alipay_dict()
            else:
                params['can_retry'] = self.can_retry
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditRiskInfo()
        if 'can_retry' in d:
            o.can_retry = d['can_retry']
        if 'code' in d:
            o.code = d['code']
        if 'data' in d:
            o.data = d['data']
        return o


