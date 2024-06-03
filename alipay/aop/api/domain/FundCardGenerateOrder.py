#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FundCardGenerateOrder(object):

    def __init__(self):
        self._denomination = None
        self._expiration_date = None
        self._quantity = None

    @property
    def denomination(self):
        return self._denomination

    @denomination.setter
    def denomination(self, value):
        self._denomination = value
    @property
    def expiration_date(self):
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, value):
        self._expiration_date = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value


    def to_alipay_dict(self):
        params = dict()
        if self.denomination:
            if hasattr(self.denomination, 'to_alipay_dict'):
                params['denomination'] = self.denomination.to_alipay_dict()
            else:
                params['denomination'] = self.denomination
        if self.expiration_date:
            if hasattr(self.expiration_date, 'to_alipay_dict'):
                params['expiration_date'] = self.expiration_date.to_alipay_dict()
            else:
                params['expiration_date'] = self.expiration_date
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FundCardGenerateOrder()
        if 'denomination' in d:
            o.denomination = d['denomination']
        if 'expiration_date' in d:
            o.expiration_date = d['expiration_date']
        if 'quantity' in d:
            o.quantity = d['quantity']
        return o


