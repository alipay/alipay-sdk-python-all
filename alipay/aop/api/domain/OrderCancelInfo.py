#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderCancelInfo(object):

    def __init__(self):
        self._operator = None
        self._reason = None
        self._reason_code = None

    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def reason_code(self):
        return self._reason_code

    @reason_code.setter
    def reason_code(self, value):
        self._reason_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        if self.reason_code:
            if hasattr(self.reason_code, 'to_alipay_dict'):
                params['reason_code'] = self.reason_code.to_alipay_dict()
            else:
                params['reason_code'] = self.reason_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderCancelInfo()
        if 'operator' in d:
            o.operator = d['operator']
        if 'reason' in d:
            o.reason = d['reason']
        if 'reason_code' in d:
            o.reason_code = d['reason_code']
        return o


