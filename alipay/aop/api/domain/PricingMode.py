#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PricingMode(object):

    def __init__(self):
        self._billing_mode = None
        self._price = None
        self._quota_unit = None

    @property
    def billing_mode(self):
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, value):
        self._billing_mode = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def quota_unit(self):
        return self._quota_unit

    @quota_unit.setter
    def quota_unit(self, value):
        self._quota_unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.billing_mode:
            if hasattr(self.billing_mode, 'to_alipay_dict'):
                params['billing_mode'] = self.billing_mode.to_alipay_dict()
            else:
                params['billing_mode'] = self.billing_mode
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.quota_unit:
            if hasattr(self.quota_unit, 'to_alipay_dict'):
                params['quota_unit'] = self.quota_unit.to_alipay_dict()
            else:
                params['quota_unit'] = self.quota_unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PricingMode()
        if 'billing_mode' in d:
            o.billing_mode = d['billing_mode']
        if 'price' in d:
            o.price = d['price']
        if 'quota_unit' in d:
            o.quota_unit = d['quota_unit']
        return o


