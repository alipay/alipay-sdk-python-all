#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PriceInformation import PriceInformation


class PaymentInformation(object):

    def __init__(self):
        self._action = None
        self._amount = None
        self._request_no = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if isinstance(value, PriceInformation):
            self._amount = value
        else:
            self._amount = PriceInformation.from_alipay_dict(value)
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
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
        o = PaymentInformation()
        if 'action' in d:
            o.action = d['action']
        if 'amount' in d:
            o.amount = d['amount']
        if 'request_no' in d:
            o.request_no = d['request_no']
        return o


