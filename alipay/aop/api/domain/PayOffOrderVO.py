#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PayOffOrderVO(object):

    def __init__(self):
        self._balance = None
        self._currency = None
        self._high_priority = None
        self._pay_off_no = None
        self._status = None

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def high_priority(self):
        return self._high_priority

    @high_priority.setter
    def high_priority(self, value):
        self._high_priority = value
    @property
    def pay_off_no(self):
        return self._pay_off_no

    @pay_off_no.setter
    def pay_off_no(self, value):
        self._pay_off_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.balance:
            if hasattr(self.balance, 'to_alipay_dict'):
                params['balance'] = self.balance.to_alipay_dict()
            else:
                params['balance'] = self.balance
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.high_priority:
            if hasattr(self.high_priority, 'to_alipay_dict'):
                params['high_priority'] = self.high_priority.to_alipay_dict()
            else:
                params['high_priority'] = self.high_priority
        if self.pay_off_no:
            if hasattr(self.pay_off_no, 'to_alipay_dict'):
                params['pay_off_no'] = self.pay_off_no.to_alipay_dict()
            else:
                params['pay_off_no'] = self.pay_off_no
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PayOffOrderVO()
        if 'balance' in d:
            o.balance = d['balance']
        if 'currency' in d:
            o.currency = d['currency']
        if 'high_priority' in d:
            o.high_priority = d['high_priority']
        if 'pay_off_no' in d:
            o.pay_off_no = d['pay_off_no']
        if 'status' in d:
            o.status = d['status']
        return o


