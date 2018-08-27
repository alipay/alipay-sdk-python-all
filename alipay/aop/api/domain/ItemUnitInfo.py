#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemUnitInfo(object):

    def __init__(self):
        self._amount = None
        self._price = None
        self._spec = None
        self._title = None
        self._unit = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def spec(self):
        return self._spec

    @spec.setter
    def spec(self, value):
        self._spec = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
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
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.spec:
            if hasattr(self.spec, 'to_alipay_dict'):
                params['spec'] = self.spec.to_alipay_dict()
            else:
                params['spec'] = self.spec
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
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
        o = ItemUnitInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'price' in d:
            o.price = d['price']
        if 'spec' in d:
            o.spec = d['spec']
        if 'title' in d:
            o.title = d['title']
        if 'unit' in d:
            o.unit = d['unit']
        return o


