#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CallUserInfo(object):

    def __init__(self):
        self._amount_overdue = None
        self._customer_name = None
        self._order_code = None
        self._phone_number = None
        self._sign_url = None

    @property
    def amount_overdue(self):
        return self._amount_overdue

    @amount_overdue.setter
    def amount_overdue(self, value):
        self._amount_overdue = value
    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, value):
        self._customer_name = value
    @property
    def order_code(self):
        return self._order_code

    @order_code.setter
    def order_code(self, value):
        self._order_code = value
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value
    @property
    def sign_url(self):
        return self._sign_url

    @sign_url.setter
    def sign_url(self, value):
        self._sign_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount_overdue:
            if hasattr(self.amount_overdue, 'to_alipay_dict'):
                params['amount_overdue'] = self.amount_overdue.to_alipay_dict()
            else:
                params['amount_overdue'] = self.amount_overdue
        if self.customer_name:
            if hasattr(self.customer_name, 'to_alipay_dict'):
                params['customer_name'] = self.customer_name.to_alipay_dict()
            else:
                params['customer_name'] = self.customer_name
        if self.order_code:
            if hasattr(self.order_code, 'to_alipay_dict'):
                params['order_code'] = self.order_code.to_alipay_dict()
            else:
                params['order_code'] = self.order_code
        if self.phone_number:
            if hasattr(self.phone_number, 'to_alipay_dict'):
                params['phone_number'] = self.phone_number.to_alipay_dict()
            else:
                params['phone_number'] = self.phone_number
        if self.sign_url:
            if hasattr(self.sign_url, 'to_alipay_dict'):
                params['sign_url'] = self.sign_url.to_alipay_dict()
            else:
                params['sign_url'] = self.sign_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CallUserInfo()
        if 'amount_overdue' in d:
            o.amount_overdue = d['amount_overdue']
        if 'customer_name' in d:
            o.customer_name = d['customer_name']
        if 'order_code' in d:
            o.order_code = d['order_code']
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        if 'sign_url' in d:
            o.sign_url = d['sign_url']
        return o


