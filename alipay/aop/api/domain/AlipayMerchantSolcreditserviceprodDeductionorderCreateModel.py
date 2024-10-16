#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantSolcreditserviceprodDeductionorderCreateModel(object):

    def __init__(self):
        self._deduction_amount = None
        self._deduction_reason = None
        self._deduction_type = None
        self._order_no = None
        self._request_no = None

    @property
    def deduction_amount(self):
        return self._deduction_amount

    @deduction_amount.setter
    def deduction_amount(self, value):
        self._deduction_amount = value
    @property
    def deduction_reason(self):
        return self._deduction_reason

    @deduction_reason.setter
    def deduction_reason(self, value):
        self._deduction_reason = value
    @property
    def deduction_type(self):
        return self._deduction_type

    @deduction_type.setter
    def deduction_type(self, value):
        self._deduction_type = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.deduction_amount:
            if hasattr(self.deduction_amount, 'to_alipay_dict'):
                params['deduction_amount'] = self.deduction_amount.to_alipay_dict()
            else:
                params['deduction_amount'] = self.deduction_amount
        if self.deduction_reason:
            if hasattr(self.deduction_reason, 'to_alipay_dict'):
                params['deduction_reason'] = self.deduction_reason.to_alipay_dict()
            else:
                params['deduction_reason'] = self.deduction_reason
        if self.deduction_type:
            if hasattr(self.deduction_type, 'to_alipay_dict'):
                params['deduction_type'] = self.deduction_type.to_alipay_dict()
            else:
                params['deduction_type'] = self.deduction_type
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
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
        o = AlipayMerchantSolcreditserviceprodDeductionorderCreateModel()
        if 'deduction_amount' in d:
            o.deduction_amount = d['deduction_amount']
        if 'deduction_reason' in d:
            o.deduction_reason = d['deduction_reason']
        if 'deduction_type' in d:
            o.deduction_type = d['deduction_type']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'request_no' in d:
            o.request_no = d['request_no']
        return o


