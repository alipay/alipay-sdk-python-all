#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbdishCookPriceInfo(object):

    def __init__(self):
        self._cook_id = None
        self._dish_id = None
        self._member_price = None
        self._sell_price = None
        self._sku_id = None

    @property
    def cook_id(self):
        return self._cook_id

    @cook_id.setter
    def cook_id(self, value):
        self._cook_id = value
    @property
    def dish_id(self):
        return self._dish_id

    @dish_id.setter
    def dish_id(self, value):
        self._dish_id = value
    @property
    def member_price(self):
        return self._member_price

    @member_price.setter
    def member_price(self, value):
        self._member_price = value
    @property
    def sell_price(self):
        return self._sell_price

    @sell_price.setter
    def sell_price(self, value):
        self._sell_price = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cook_id:
            if hasattr(self.cook_id, 'to_alipay_dict'):
                params['cook_id'] = self.cook_id.to_alipay_dict()
            else:
                params['cook_id'] = self.cook_id
        if self.dish_id:
            if hasattr(self.dish_id, 'to_alipay_dict'):
                params['dish_id'] = self.dish_id.to_alipay_dict()
            else:
                params['dish_id'] = self.dish_id
        if self.member_price:
            if hasattr(self.member_price, 'to_alipay_dict'):
                params['member_price'] = self.member_price.to_alipay_dict()
            else:
                params['member_price'] = self.member_price
        if self.sell_price:
            if hasattr(self.sell_price, 'to_alipay_dict'):
                params['sell_price'] = self.sell_price.to_alipay_dict()
            else:
                params['sell_price'] = self.sell_price
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
        o = KbdishCookPriceInfo()
        if 'cook_id' in d:
            o.cook_id = d['cook_id']
        if 'dish_id' in d:
            o.dish_id = d['dish_id']
        if 'member_price' in d:
            o.member_price = d['member_price']
        if 'sell_price' in d:
            o.sell_price = d['sell_price']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        return o


