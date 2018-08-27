#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MCardDetail(object):

    def __init__(self):
        self._available_amount = None
        self._name = None
        self._pay_amount = None

    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        self._available_amount = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.available_amount:
            if hasattr(self.available_amount, 'to_alipay_dict'):
                params['available_amount'] = self.available_amount.to_alipay_dict()
            else:
                params['available_amount'] = self.available_amount
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MCardDetail()
        if 'available_amount' in d:
            o.available_amount = d['available_amount']
        if 'name' in d:
            o.name = d['name']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        return o


