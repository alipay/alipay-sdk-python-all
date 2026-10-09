#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChargeOption(object):

    def __init__(self):
        self._display_name = None
        self._duration_period = None
        self._price = None
        self._quota_amount = None
        self._sku_id = None

    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        self._display_name = value
    @property
    def duration_period(self):
        return self._duration_period

    @duration_period.setter
    def duration_period(self, value):
        self._duration_period = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def quota_amount(self):
        return self._quota_amount

    @quota_amount.setter
    def quota_amount(self, value):
        self._quota_amount = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.display_name:
            if hasattr(self.display_name, 'to_alipay_dict'):
                params['display_name'] = self.display_name.to_alipay_dict()
            else:
                params['display_name'] = self.display_name
        if self.duration_period:
            if hasattr(self.duration_period, 'to_alipay_dict'):
                params['duration_period'] = self.duration_period.to_alipay_dict()
            else:
                params['duration_period'] = self.duration_period
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.quota_amount:
            if hasattr(self.quota_amount, 'to_alipay_dict'):
                params['quota_amount'] = self.quota_amount.to_alipay_dict()
            else:
                params['quota_amount'] = self.quota_amount
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChargeOption()
        if 'display_name' in d:
            o.display_name = d['display_name']
        if 'duration_period' in d:
            o.duration_period = d['duration_period']
        if 'price' in d:
            o.price = d['price']
        if 'quota_amount' in d:
            o.quota_amount = d['quota_amount']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        return o


