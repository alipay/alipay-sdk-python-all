#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantSolcreditserviceprodDeductionorderRefundModel(object):

    def __init__(self):
        self._amount = None
        self._deduction_order_no = None
        self._request_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def deduction_order_no(self):
        return self._deduction_order_no

    @deduction_order_no.setter
    def deduction_order_no(self, value):
        self._deduction_order_no = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.deduction_order_no:
            if hasattr(self.deduction_order_no, 'to_alipay_dict'):
                params['deduction_order_no'] = self.deduction_order_no.to_alipay_dict()
            else:
                params['deduction_order_no'] = self.deduction_order_no
        if self.request_no:
            if hasattr(self.request_no, 'to_alipay_dict'):
                params['request_no'] = self.request_no.to_alipay_dict()
            else:
                params['request_no'] = self.request_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantSolcreditserviceprodDeductionorderRefundModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'deduction_order_no' in d:
            o.deduction_order_no = d['deduction_order_no']
        if 'request_no' in d:
            o.request_no = d['request_no']
        return o


