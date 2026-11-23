#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PricingModeForList(object):

    def __init__(self):
        self._billing_mode = None
        self._currency = None
        self._display_name = None
        self._duration_period = None
        self._price = None
        self._quota_amount = None
        self._quota_unit = None

    @property
    def billing_mode(self):
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, value):
        self._billing_mode = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
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
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
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
        o = PricingModeForList()
        if 'billing_mode' in d:
            o.billing_mode = d['billing_mode']
        if 'currency' in d:
            o.currency = d['currency']
        if 'display_name' in d:
            o.display_name = d['display_name']
        if 'duration_period' in d:
            o.duration_period = d['duration_period']
        if 'price' in d:
            o.price = d['price']
        if 'quota_amount' in d:
            o.quota_amount = d['quota_amount']
        if 'quota_unit' in d:
            o.quota_unit = d['quota_unit']
        return o


