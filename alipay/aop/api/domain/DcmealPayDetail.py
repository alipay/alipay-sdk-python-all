#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DcmealPayDetail(object):

    def __init__(self):
        self._amount = None
        self._trace_no = None
        self._type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def trace_no(self):
        return self._trace_no

    @trace_no.setter
    def trace_no(self, value):
        self._trace_no = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.trace_no:
            if hasattr(self.trace_no, 'to_alipay_dict'):
                params['trace_no'] = self.trace_no.to_alipay_dict()
            else:
                params['trace_no'] = self.trace_no
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DcmealPayDetail()
        if 'amount' in d:
            o.amount = d['amount']
        if 'trace_no' in d:
            o.trace_no = d['trace_no']
        if 'type' in d:
            o.type = d['type']
        return o


