#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CertificateItem(object):

    def __init__(self):
        self._code = None
        self._out_code = None
        self._refund_amount = None
        self._total_times = None
        self._used_times = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def out_code(self):
        return self._out_code

    @out_code.setter
    def out_code(self, value):
        self._out_code = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def total_times(self):
        return self._total_times

    @total_times.setter
    def total_times(self, value):
        self._total_times = value
    @property
    def used_times(self):
        return self._used_times

    @used_times.setter
    def used_times(self, value):
        self._used_times = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.out_code:
            if hasattr(self.out_code, 'to_alipay_dict'):
                params['out_code'] = self.out_code.to_alipay_dict()
            else:
                params['out_code'] = self.out_code
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.total_times:
            if hasattr(self.total_times, 'to_alipay_dict'):
                params['total_times'] = self.total_times.to_alipay_dict()
            else:
                params['total_times'] = self.total_times
        if self.used_times:
            if hasattr(self.used_times, 'to_alipay_dict'):
                params['used_times'] = self.used_times.to_alipay_dict()
            else:
                params['used_times'] = self.used_times
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CertificateItem()
        if 'code' in d:
            o.code = d['code']
        if 'out_code' in d:
            o.out_code = d['out_code']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'total_times' in d:
            o.total_times = d['total_times']
        if 'used_times' in d:
            o.used_times = d['used_times']
        return o


