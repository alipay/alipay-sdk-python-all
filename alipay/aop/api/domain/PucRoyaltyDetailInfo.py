#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PucRoyaltyDetailInfo(object):

    def __init__(self):
        self._amount = None
        self._trans_in = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def trans_in(self):
        return self._trans_in

    @trans_in.setter
    def trans_in(self, value):
        self._trans_in = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.trans_in:
            if hasattr(self.trans_in, 'to_alipay_dict'):
                params['trans_in'] = self.trans_in.to_alipay_dict()
            else:
                params['trans_in'] = self.trans_in
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PucRoyaltyDetailInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'trans_in' in d:
            o.trans_in = d['trans_in']
        return o


