#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoicePaymentInfo(object):

    def __init__(self):
        self._biz_order_amount = None
        self._biz_order_no = None
        self._biz_order_type = None
        self._payment_amount = None
        self._payment_order_no = None
        self._payment_order_type = None

    @property
    def biz_order_amount(self):
        return self._biz_order_amount

    @biz_order_amount.setter
    def biz_order_amount(self, value):
        self._biz_order_amount = value
    @property
    def biz_order_no(self):
        return self._biz_order_no

    @biz_order_no.setter
    def biz_order_no(self, value):
        self._biz_order_no = value
    @property
    def biz_order_type(self):
        return self._biz_order_type

    @biz_order_type.setter
    def biz_order_type(self, value):
        self._biz_order_type = value
    @property
    def payment_amount(self):
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self._payment_amount = value
    @property
    def payment_order_no(self):
        return self._payment_order_no

    @payment_order_no.setter
    def payment_order_no(self, value):
        self._payment_order_no = value
    @property
    def payment_order_type(self):
        return self._payment_order_type

    @payment_order_type.setter
    def payment_order_type(self, value):
        self._payment_order_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_order_amount:
            if hasattr(self.biz_order_amount, 'to_alipay_dict'):
                params['biz_order_amount'] = self.biz_order_amount.to_alipay_dict()
            else:
                params['biz_order_amount'] = self.biz_order_amount
        if self.biz_order_no:
            if hasattr(self.biz_order_no, 'to_alipay_dict'):
                params['biz_order_no'] = self.biz_order_no.to_alipay_dict()
            else:
                params['biz_order_no'] = self.biz_order_no
        if self.biz_order_type:
            if hasattr(self.biz_order_type, 'to_alipay_dict'):
                params['biz_order_type'] = self.biz_order_type.to_alipay_dict()
            else:
                params['biz_order_type'] = self.biz_order_type
        if self.payment_amount:
            if hasattr(self.payment_amount, 'to_alipay_dict'):
                params['payment_amount'] = self.payment_amount.to_alipay_dict()
            else:
                params['payment_amount'] = self.payment_amount
        if self.payment_order_no:
            if hasattr(self.payment_order_no, 'to_alipay_dict'):
                params['payment_order_no'] = self.payment_order_no.to_alipay_dict()
            else:
                params['payment_order_no'] = self.payment_order_no
        if self.payment_order_type:
            if hasattr(self.payment_order_type, 'to_alipay_dict'):
                params['payment_order_type'] = self.payment_order_type.to_alipay_dict()
            else:
                params['payment_order_type'] = self.payment_order_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoicePaymentInfo()
        if 'biz_order_amount' in d:
            o.biz_order_amount = d['biz_order_amount']
        if 'biz_order_no' in d:
            o.biz_order_no = d['biz_order_no']
        if 'biz_order_type' in d:
            o.biz_order_type = d['biz_order_type']
        if 'payment_amount' in d:
            o.payment_amount = d['payment_amount']
        if 'payment_order_no' in d:
            o.payment_order_no = d['payment_order_no']
        if 'payment_order_type' in d:
            o.payment_order_type = d['payment_order_type']
        return o


