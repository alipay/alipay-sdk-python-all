#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PaymentAccountInfo(object):

    def __init__(self):
        self._account_name = None
        self._account_no = None
        self._account_type = None
        self._amount = None
        self._content = None

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaymentAccountInfo()
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'amount' in d:
            o.amount = d['amount']
        if 'content' in d:
            o.content = d['content']
        return o


