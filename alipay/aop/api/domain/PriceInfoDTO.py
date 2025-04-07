#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PriceInfoDTO(object):

    def __init__(self):
        self._additional_price = None
        self._discounted_price = None
        self._freight = None
        self._max_order_price = None
        self._merchant_value_price = None
        self._min_order_price = None
        self._order_price = None
        self._price_mode = None

    @property
    def additional_price(self):
        return self._additional_price

    @additional_price.setter
    def additional_price(self, value):
        self._additional_price = value
    @property
    def discounted_price(self):
        return self._discounted_price

    @discounted_price.setter
    def discounted_price(self, value):
        self._discounted_price = value
    @property
    def freight(self):
        return self._freight

    @freight.setter
    def freight(self, value):
        self._freight = value
    @property
    def max_order_price(self):
        return self._max_order_price

    @max_order_price.setter
    def max_order_price(self, value):
        self._max_order_price = value
    @property
    def merchant_value_price(self):
        return self._merchant_value_price

    @merchant_value_price.setter
    def merchant_value_price(self, value):
        self._merchant_value_price = value
    @property
    def min_order_price(self):
        return self._min_order_price

    @min_order_price.setter
    def min_order_price(self, value):
        self._min_order_price = value
    @property
    def order_price(self):
        return self._order_price

    @order_price.setter
    def order_price(self, value):
        self._order_price = value
    @property
    def price_mode(self):
        return self._price_mode

    @price_mode.setter
    def price_mode(self, value):
        self._price_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.additional_price:
            if hasattr(self.additional_price, 'to_alipay_dict'):
                params['additional_price'] = self.additional_price.to_alipay_dict()
            else:
                params['additional_price'] = self.additional_price
        if self.discounted_price:
            if hasattr(self.discounted_price, 'to_alipay_dict'):
                params['discounted_price'] = self.discounted_price.to_alipay_dict()
            else:
                params['discounted_price'] = self.discounted_price
        if self.freight:
            if hasattr(self.freight, 'to_alipay_dict'):
                params['freight'] = self.freight.to_alipay_dict()
            else:
                params['freight'] = self.freight
        if self.max_order_price:
            if hasattr(self.max_order_price, 'to_alipay_dict'):
                params['max_order_price'] = self.max_order_price.to_alipay_dict()
            else:
                params['max_order_price'] = self.max_order_price
        if self.merchant_value_price:
            if hasattr(self.merchant_value_price, 'to_alipay_dict'):
                params['merchant_value_price'] = self.merchant_value_price.to_alipay_dict()
            else:
                params['merchant_value_price'] = self.merchant_value_price
        if self.min_order_price:
            if hasattr(self.min_order_price, 'to_alipay_dict'):
                params['min_order_price'] = self.min_order_price.to_alipay_dict()
            else:
                params['min_order_price'] = self.min_order_price
        if self.order_price:
            if hasattr(self.order_price, 'to_alipay_dict'):
                params['order_price'] = self.order_price.to_alipay_dict()
            else:
                params['order_price'] = self.order_price
        if self.price_mode:
            if hasattr(self.price_mode, 'to_alipay_dict'):
                params['price_mode'] = self.price_mode.to_alipay_dict()
            else:
                params['price_mode'] = self.price_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PriceInfoDTO()
        if 'additional_price' in d:
            o.additional_price = d['additional_price']
        if 'discounted_price' in d:
            o.discounted_price = d['discounted_price']
        if 'freight' in d:
            o.freight = d['freight']
        if 'max_order_price' in d:
            o.max_order_price = d['max_order_price']
        if 'merchant_value_price' in d:
            o.merchant_value_price = d['merchant_value_price']
        if 'min_order_price' in d:
            o.min_order_price = d['min_order_price']
        if 'order_price' in d:
            o.order_price = d['order_price']
        if 'price_mode' in d:
            o.price_mode = d['price_mode']
        return o


