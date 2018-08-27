#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EcoRenthouseOtherAmount(object):

    def __init__(self):
        self._amount = None
        self._name = None
        self._unit = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.unit:
            if hasattr(self.unit, 'to_alipay_dict'):
                params['unit'] = self.unit.to_alipay_dict()
            else:
                params['unit'] = self.unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcoRenthouseOtherAmount()
        if 'amount' in d:
            o.amount = d['amount']
        if 'name' in d:
            o.name = d['name']
        if 'unit' in d:
            o.unit = d['unit']
        return o


