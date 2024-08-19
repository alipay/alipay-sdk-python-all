#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentCarRefundItem(object):

    def __init__(self):
        self._refund_amount = None
        self._refund_result = None
        self._trade_no = None

    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_result(self):
        return self._refund_result

    @refund_result.setter
    def refund_result(self, value):
        self._refund_result = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_result:
            if hasattr(self.refund_result, 'to_alipay_dict'):
                params['refund_result'] = self.refund_result.to_alipay_dict()
            else:
                params['refund_result'] = self.refund_result
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentCarRefundItem()
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_result' in d:
            o.refund_result = d['refund_result']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


