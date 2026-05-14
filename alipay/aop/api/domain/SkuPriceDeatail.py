#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SkuPriceDeatail(object):

    def __init__(self):
        self._consumables_price = None
        self._drug_price = None
        self._price = None
        self._sku_code = None

    @property
    def consumables_price(self):
        return self._consumables_price

    @consumables_price.setter
    def consumables_price(self, value):
        self._consumables_price = value
    @property
    def drug_price(self):
        return self._drug_price

    @drug_price.setter
    def drug_price(self, value):
        self._drug_price = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def sku_code(self):
        return self._sku_code

    @sku_code.setter
    def sku_code(self, value):
        self._sku_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.consumables_price:
            if hasattr(self.consumables_price, 'to_alipay_dict'):
                params['consumables_price'] = self.consumables_price.to_alipay_dict()
            else:
                params['consumables_price'] = self.consumables_price
        if self.drug_price:
            if hasattr(self.drug_price, 'to_alipay_dict'):
                params['drug_price'] = self.drug_price.to_alipay_dict()
            else:
                params['drug_price'] = self.drug_price
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.sku_code:
            if hasattr(self.sku_code, 'to_alipay_dict'):
                params['sku_code'] = self.sku_code.to_alipay_dict()
            else:
                params['sku_code'] = self.sku_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SkuPriceDeatail()
        if 'consumables_price' in d:
            o.consumables_price = d['consumables_price']
        if 'drug_price' in d:
            o.drug_price = d['drug_price']
        if 'price' in d:
            o.price = d['price']
        if 'sku_code' in d:
            o.sku_code = d['sku_code']
        return o


