#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankPaymentTradeBusinessOrderConfirmModel(object):

    def __init__(self):
        self._amount = None
        self._currency_value = None
        self._order_no = None
        self._request_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def currency_value(self):
        return self._currency_value

    @currency_value.setter
    def currency_value(self, value):
        self._currency_value = value
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
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.currency_value:
            if hasattr(self.currency_value, 'to_alipay_dict'):
                params['currency_value'] = self.currency_value.to_alipay_dict()
            else:
                params['currency_value'] = self.currency_value
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
        o = MybankPaymentTradeBusinessOrderConfirmModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'currency_value' in d:
            o.currency_value = d['currency_value']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'request_no' in d:
            o.request_no = d['request_no']
        return o


