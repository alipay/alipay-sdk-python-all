#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RefundRoyaltyInfo(object):

    def __init__(self):
        self._memo = None
        self._refund_amount = None
        self._trans_in = None
        self._trans_in_email = None
        self._trans_out = None
        self._trans_out_email = None

    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def trans_in(self):
        return self._trans_in

    @trans_in.setter
    def trans_in(self, value):
        self._trans_in = value
    @property
    def trans_in_email(self):
        return self._trans_in_email

    @trans_in_email.setter
    def trans_in_email(self, value):
        self._trans_in_email = value
    @property
    def trans_out(self):
        return self._trans_out

    @trans_out.setter
    def trans_out(self, value):
        self._trans_out = value
    @property
    def trans_out_email(self):
        return self._trans_out_email

    @trans_out_email.setter
    def trans_out_email(self, value):
        self._trans_out_email = value


    def to_alipay_dict(self):
        params = dict()
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.trans_in:
            if hasattr(self.trans_in, 'to_alipay_dict'):
                params['trans_in'] = self.trans_in.to_alipay_dict()
            else:
                params['trans_in'] = self.trans_in
        if self.trans_in_email:
            if hasattr(self.trans_in_email, 'to_alipay_dict'):
                params['trans_in_email'] = self.trans_in_email.to_alipay_dict()
            else:
                params['trans_in_email'] = self.trans_in_email
        if self.trans_out:
            if hasattr(self.trans_out, 'to_alipay_dict'):
                params['trans_out'] = self.trans_out.to_alipay_dict()
            else:
                params['trans_out'] = self.trans_out
        if self.trans_out_email:
            if hasattr(self.trans_out_email, 'to_alipay_dict'):
                params['trans_out_email'] = self.trans_out_email.to_alipay_dict()
            else:
                params['trans_out_email'] = self.trans_out_email
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RefundRoyaltyInfo()
        if 'memo' in d:
            o.memo = d['memo']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'trans_in' in d:
            o.trans_in = d['trans_in']
        if 'trans_in_email' in d:
            o.trans_in_email = d['trans_in_email']
        if 'trans_out' in d:
            o.trans_out = d['trans_out']
        if 'trans_out_email' in d:
            o.trans_out_email = d['trans_out_email']
        return o


