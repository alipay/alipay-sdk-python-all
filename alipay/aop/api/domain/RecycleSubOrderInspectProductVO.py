#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleSubOrderInspectProductVO(object):

    def __init__(self):
        self._inspect_price = None
        self._product_code = None
        self._product_unique_id = None
        self._real_unit_pricing = None

    @property
    def inspect_price(self):
        return self._inspect_price

    @inspect_price.setter
    def inspect_price(self, value):
        self._inspect_price = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def product_unique_id(self):
        return self._product_unique_id

    @product_unique_id.setter
    def product_unique_id(self, value):
        self._product_unique_id = value
    @property
    def real_unit_pricing(self):
        return self._real_unit_pricing

    @real_unit_pricing.setter
    def real_unit_pricing(self, value):
        self._real_unit_pricing = value


    def to_alipay_dict(self):
        params = dict()
        if self.inspect_price:
            if hasattr(self.inspect_price, 'to_alipay_dict'):
                params['inspect_price'] = self.inspect_price.to_alipay_dict()
            else:
                params['inspect_price'] = self.inspect_price
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.product_unique_id:
            if hasattr(self.product_unique_id, 'to_alipay_dict'):
                params['product_unique_id'] = self.product_unique_id.to_alipay_dict()
            else:
                params['product_unique_id'] = self.product_unique_id
        if self.real_unit_pricing:
            if hasattr(self.real_unit_pricing, 'to_alipay_dict'):
                params['real_unit_pricing'] = self.real_unit_pricing.to_alipay_dict()
            else:
                params['real_unit_pricing'] = self.real_unit_pricing
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleSubOrderInspectProductVO()
        if 'inspect_price' in d:
            o.inspect_price = d['inspect_price']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'product_unique_id' in d:
            o.product_unique_id = d['product_unique_id']
        if 'real_unit_pricing' in d:
            o.real_unit_pricing = d['real_unit_pricing']
        return o


