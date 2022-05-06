#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HbGoodsTradeRule(object):

    def __init__(self):
        self._max_buy_frequency = None
        self._max_buy_quantity = None
        self._min_buy_quantity = None
        self._one_max_quantity = None
        self._service_fee_ratio = None

    @property
    def max_buy_frequency(self):
        return self._max_buy_frequency

    @max_buy_frequency.setter
    def max_buy_frequency(self, value):
        self._max_buy_frequency = value
    @property
    def max_buy_quantity(self):
        return self._max_buy_quantity

    @max_buy_quantity.setter
    def max_buy_quantity(self, value):
        self._max_buy_quantity = value
    @property
    def min_buy_quantity(self):
        return self._min_buy_quantity

    @min_buy_quantity.setter
    def min_buy_quantity(self, value):
        self._min_buy_quantity = value
    @property
    def one_max_quantity(self):
        return self._one_max_quantity

    @one_max_quantity.setter
    def one_max_quantity(self, value):
        self._one_max_quantity = value
    @property
    def service_fee_ratio(self):
        return self._service_fee_ratio

    @service_fee_ratio.setter
    def service_fee_ratio(self, value):
        self._service_fee_ratio = value


    def to_alipay_dict(self):
        params = dict()
        if self.max_buy_frequency:
            if hasattr(self.max_buy_frequency, 'to_alipay_dict'):
                params['max_buy_frequency'] = self.max_buy_frequency.to_alipay_dict()
            else:
                params['max_buy_frequency'] = self.max_buy_frequency
        if self.max_buy_quantity:
            if hasattr(self.max_buy_quantity, 'to_alipay_dict'):
                params['max_buy_quantity'] = self.max_buy_quantity.to_alipay_dict()
            else:
                params['max_buy_quantity'] = self.max_buy_quantity
        if self.min_buy_quantity:
            if hasattr(self.min_buy_quantity, 'to_alipay_dict'):
                params['min_buy_quantity'] = self.min_buy_quantity.to_alipay_dict()
            else:
                params['min_buy_quantity'] = self.min_buy_quantity
        if self.one_max_quantity:
            if hasattr(self.one_max_quantity, 'to_alipay_dict'):
                params['one_max_quantity'] = self.one_max_quantity.to_alipay_dict()
            else:
                params['one_max_quantity'] = self.one_max_quantity
        if self.service_fee_ratio:
            if hasattr(self.service_fee_ratio, 'to_alipay_dict'):
                params['service_fee_ratio'] = self.service_fee_ratio.to_alipay_dict()
            else:
                params['service_fee_ratio'] = self.service_fee_ratio
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HbGoodsTradeRule()
        if 'max_buy_frequency' in d:
            o.max_buy_frequency = d['max_buy_frequency']
        if 'max_buy_quantity' in d:
            o.max_buy_quantity = d['max_buy_quantity']
        if 'min_buy_quantity' in d:
            o.min_buy_quantity = d['min_buy_quantity']
        if 'one_max_quantity' in d:
            o.one_max_quantity = d['one_max_quantity']
        if 'service_fee_ratio' in d:
            o.service_fee_ratio = d['service_fee_ratio']
        return o


