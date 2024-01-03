#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentCarFeeItem(object):

    def __init__(self):
        self._amount = None
        self._desc = None
        self._name = None
        self._unique_code = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def unique_code(self):
        return self._unique_code

    @unique_code.setter
    def unique_code(self, value):
        self._unique_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.unique_code:
            if hasattr(self.unique_code, 'to_alipay_dict'):
                params['unique_code'] = self.unique_code.to_alipay_dict()
            else:
                params['unique_code'] = self.unique_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentCarFeeItem()
        if 'amount' in d:
            o.amount = d['amount']
        if 'desc' in d:
            o.desc = d['desc']
        if 'name' in d:
            o.name = d['name']
        if 'unique_code' in d:
            o.unique_code = d['unique_code']
        return o


