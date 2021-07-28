#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RateCurrency(object):

    def __init__(self):
        self._currency = None
        self._currency_chinese_name = None
        self._currency_icon = None

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def currency_chinese_name(self):
        return self._currency_chinese_name

    @currency_chinese_name.setter
    def currency_chinese_name(self, value):
        self._currency_chinese_name = value
    @property
    def currency_icon(self):
        return self._currency_icon

    @currency_icon.setter
    def currency_icon(self, value):
        self._currency_icon = value


    def to_alipay_dict(self):
        params = dict()
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.currency_chinese_name:
            if hasattr(self.currency_chinese_name, 'to_alipay_dict'):
                params['currency_chinese_name'] = self.currency_chinese_name.to_alipay_dict()
            else:
                params['currency_chinese_name'] = self.currency_chinese_name
        if self.currency_icon:
            if hasattr(self.currency_icon, 'to_alipay_dict'):
                params['currency_icon'] = self.currency_icon.to_alipay_dict()
            else:
                params['currency_icon'] = self.currency_icon
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RateCurrency()
        if 'currency' in d:
            o.currency = d['currency']
        if 'currency_chinese_name' in d:
            o.currency_chinese_name = d['currency_chinese_name']
        if 'currency_icon' in d:
            o.currency_icon = d['currency_icon']
        return o


