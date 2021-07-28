#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TuitionRefundRoyaltyInfo(object):

    def __init__(self):
        self._amount = None
        self._amount_percent = None
        self._royalty_type = None
        self._trans_in = None
        self._trans_out = None
        self._trans_type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def amount_percent(self):
        return self._amount_percent

    @amount_percent.setter
    def amount_percent(self, value):
        self._amount_percent = value
    @property
    def royalty_type(self):
        return self._royalty_type

    @royalty_type.setter
    def royalty_type(self, value):
        self._royalty_type = value
    @property
    def trans_in(self):
        return self._trans_in

    @trans_in.setter
    def trans_in(self, value):
        self._trans_in = value
    @property
    def trans_out(self):
        return self._trans_out

    @trans_out.setter
    def trans_out(self, value):
        self._trans_out = value
    @property
    def trans_type(self):
        return self._trans_type

    @trans_type.setter
    def trans_type(self, value):
        self._trans_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.amount_percent:
            if hasattr(self.amount_percent, 'to_alipay_dict'):
                params['amount_percent'] = self.amount_percent.to_alipay_dict()
            else:
                params['amount_percent'] = self.amount_percent
        if self.royalty_type:
            if hasattr(self.royalty_type, 'to_alipay_dict'):
                params['royalty_type'] = self.royalty_type.to_alipay_dict()
            else:
                params['royalty_type'] = self.royalty_type
        if self.trans_in:
            if hasattr(self.trans_in, 'to_alipay_dict'):
                params['trans_in'] = self.trans_in.to_alipay_dict()
            else:
                params['trans_in'] = self.trans_in
        if self.trans_out:
            if hasattr(self.trans_out, 'to_alipay_dict'):
                params['trans_out'] = self.trans_out.to_alipay_dict()
            else:
                params['trans_out'] = self.trans_out
        if self.trans_type:
            if hasattr(self.trans_type, 'to_alipay_dict'):
                params['trans_type'] = self.trans_type.to_alipay_dict()
            else:
                params['trans_type'] = self.trans_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TuitionRefundRoyaltyInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'amount_percent' in d:
            o.amount_percent = d['amount_percent']
        if 'royalty_type' in d:
            o.royalty_type = d['royalty_type']
        if 'trans_in' in d:
            o.trans_in = d['trans_in']
        if 'trans_out' in d:
            o.trans_out = d['trans_out']
        if 'trans_type' in d:
            o.trans_type = d['trans_type']
        return o


