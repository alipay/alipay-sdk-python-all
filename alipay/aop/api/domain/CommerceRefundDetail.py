#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CommerceRefundDetail(object):

    def __init__(self):
        self._pay_trade_no = None
        self._refund_amount = None
        self._refund_request_no = None
        self._status = None

    @property
    def pay_trade_no(self):
        return self._pay_trade_no

    @pay_trade_no.setter
    def pay_trade_no(self, value):
        self._pay_trade_no = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_request_no(self):
        return self._refund_request_no

    @refund_request_no.setter
    def refund_request_no(self, value):
        self._refund_request_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.pay_trade_no:
            if hasattr(self.pay_trade_no, 'to_alipay_dict'):
                params['pay_trade_no'] = self.pay_trade_no.to_alipay_dict()
            else:
                params['pay_trade_no'] = self.pay_trade_no
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_request_no:
            if hasattr(self.refund_request_no, 'to_alipay_dict'):
                params['refund_request_no'] = self.refund_request_no.to_alipay_dict()
            else:
                params['refund_request_no'] = self.refund_request_no
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommerceRefundDetail()
        if 'pay_trade_no' in d:
            o.pay_trade_no = d['pay_trade_no']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_request_no' in d:
            o.refund_request_no = d['refund_request_no']
        if 'status' in d:
            o.status = d['status']
        return o


