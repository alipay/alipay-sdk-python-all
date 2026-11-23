#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PayBillInfo(object):

    def __init__(self):
        self._bill_amount = None
        self._bill_total_amount = None
        self._order_source = None
        self._total_discount_amount = None
        self._user_pay_amount = None

    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        self._bill_amount = value
    @property
    def bill_total_amount(self):
        return self._bill_total_amount

    @bill_total_amount.setter
    def bill_total_amount(self, value):
        self._bill_total_amount = value
    @property
    def order_source(self):
        return self._order_source

    @order_source.setter
    def order_source(self, value):
        self._order_source = value
    @property
    def total_discount_amount(self):
        return self._total_discount_amount

    @total_discount_amount.setter
    def total_discount_amount(self, value):
        self._total_discount_amount = value
    @property
    def user_pay_amount(self):
        return self._user_pay_amount

    @user_pay_amount.setter
    def user_pay_amount(self, value):
        self._user_pay_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_amount:
            if hasattr(self.bill_amount, 'to_alipay_dict'):
                params['bill_amount'] = self.bill_amount.to_alipay_dict()
            else:
                params['bill_amount'] = self.bill_amount
        if self.bill_total_amount:
            if hasattr(self.bill_total_amount, 'to_alipay_dict'):
                params['bill_total_amount'] = self.bill_total_amount.to_alipay_dict()
            else:
                params['bill_total_amount'] = self.bill_total_amount
        if self.order_source:
            if hasattr(self.order_source, 'to_alipay_dict'):
                params['order_source'] = self.order_source.to_alipay_dict()
            else:
                params['order_source'] = self.order_source
        if self.total_discount_amount:
            if hasattr(self.total_discount_amount, 'to_alipay_dict'):
                params['total_discount_amount'] = self.total_discount_amount.to_alipay_dict()
            else:
                params['total_discount_amount'] = self.total_discount_amount
        if self.user_pay_amount:
            if hasattr(self.user_pay_amount, 'to_alipay_dict'):
                params['user_pay_amount'] = self.user_pay_amount.to_alipay_dict()
            else:
                params['user_pay_amount'] = self.user_pay_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PayBillInfo()
        if 'bill_amount' in d:
            o.bill_amount = d['bill_amount']
        if 'bill_total_amount' in d:
            o.bill_total_amount = d['bill_total_amount']
        if 'order_source' in d:
            o.order_source = d['order_source']
        if 'total_discount_amount' in d:
            o.total_discount_amount = d['total_discount_amount']
        if 'user_pay_amount' in d:
            o.user_pay_amount = d['user_pay_amount']
        return o


