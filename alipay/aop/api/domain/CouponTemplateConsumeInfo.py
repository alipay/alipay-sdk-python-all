#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CouponTemplateConsumeInfo(object):

    def __init__(self):
        self._receive_amount = None
        self._receive_count = None
        self._refund_amount = None
        self._used_amount = None
        self._used_count = None

    @property
    def receive_amount(self):
        return self._receive_amount

    @receive_amount.setter
    def receive_amount(self, value):
        self._receive_amount = value
    @property
    def receive_count(self):
        return self._receive_count

    @receive_count.setter
    def receive_count(self, value):
        self._receive_count = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def used_amount(self):
        return self._used_amount

    @used_amount.setter
    def used_amount(self, value):
        self._used_amount = value
    @property
    def used_count(self):
        return self._used_count

    @used_count.setter
    def used_count(self, value):
        self._used_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.receive_amount:
            if hasattr(self.receive_amount, 'to_alipay_dict'):
                params['receive_amount'] = self.receive_amount.to_alipay_dict()
            else:
                params['receive_amount'] = self.receive_amount
        if self.receive_count:
            if hasattr(self.receive_count, 'to_alipay_dict'):
                params['receive_count'] = self.receive_count.to_alipay_dict()
            else:
                params['receive_count'] = self.receive_count
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.used_amount:
            if hasattr(self.used_amount, 'to_alipay_dict'):
                params['used_amount'] = self.used_amount.to_alipay_dict()
            else:
                params['used_amount'] = self.used_amount
        if self.used_count:
            if hasattr(self.used_count, 'to_alipay_dict'):
                params['used_count'] = self.used_count.to_alipay_dict()
            else:
                params['used_count'] = self.used_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CouponTemplateConsumeInfo()
        if 'receive_amount' in d:
            o.receive_amount = d['receive_amount']
        if 'receive_count' in d:
            o.receive_count = d['receive_count']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'used_amount' in d:
            o.used_amount = d['used_amount']
        if 'used_count' in d:
            o.used_count = d['used_count']
        return o


