#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceTradeFundItem(object):

    def __init__(self):
        self._amount = None
        self._payment_tool_name = None
        self._payment_tool_type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def payment_tool_name(self):
        return self._payment_tool_name

    @payment_tool_name.setter
    def payment_tool_name(self, value):
        self._payment_tool_name = value
    @property
    def payment_tool_type(self):
        return self._payment_tool_type

    @payment_tool_type.setter
    def payment_tool_type(self, value):
        self._payment_tool_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.payment_tool_name:
            if hasattr(self.payment_tool_name, 'to_alipay_dict'):
                params['payment_tool_name'] = self.payment_tool_name.to_alipay_dict()
            else:
                params['payment_tool_name'] = self.payment_tool_name
        if self.payment_tool_type:
            if hasattr(self.payment_tool_type, 'to_alipay_dict'):
                params['payment_tool_type'] = self.payment_tool_type.to_alipay_dict()
            else:
                params['payment_tool_type'] = self.payment_tool_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceTradeFundItem()
        if 'amount' in d:
            o.amount = d['amount']
        if 'payment_tool_name' in d:
            o.payment_tool_name = d['payment_tool_name']
        if 'payment_tool_type' in d:
            o.payment_tool_type = d['payment_tool_type']
        return o


