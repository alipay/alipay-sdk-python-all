#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RefundRoyaltyResult(object):

    def __init__(self):
        self._refund_amount = None
        self._result_code = None
        self._royalty_type = None
        self._trans_in = None
        self._trans_in_email = None
        self._trans_out = None
        self._trans_out_email = None

    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
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
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.result_code:
            if hasattr(self.result_code, 'to_alipay_dict'):
                params['result_code'] = self.result_code.to_alipay_dict()
            else:
                params['result_code'] = self.result_code
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
        o = RefundRoyaltyResult()
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'result_code' in d:
            o.result_code = d['result_code']
        if 'royalty_type' in d:
            o.royalty_type = d['royalty_type']
        if 'trans_in' in d:
            o.trans_in = d['trans_in']
        if 'trans_in_email' in d:
            o.trans_in_email = d['trans_in_email']
        if 'trans_out' in d:
            o.trans_out = d['trans_out']
        if 'trans_out_email' in d:
            o.trans_out_email = d['trans_out_email']
        return o


