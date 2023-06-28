#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CertificateInstanceAmountInfo(object):

    def __init__(self):
        self._original_price = None
        self._receipt_amount = None
        self._sale_price = None

    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def receipt_amount(self):
        return self._receipt_amount

    @receipt_amount.setter
    def receipt_amount(self, value):
        self._receipt_amount = value
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.receipt_amount:
            if hasattr(self.receipt_amount, 'to_alipay_dict'):
                params['receipt_amount'] = self.receipt_amount.to_alipay_dict()
            else:
                params['receipt_amount'] = self.receipt_amount
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CertificateInstanceAmountInfo()
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'receipt_amount' in d:
            o.receipt_amount = d['receipt_amount']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        return o


