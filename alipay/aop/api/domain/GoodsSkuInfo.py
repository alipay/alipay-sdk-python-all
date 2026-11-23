#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GoodsSkuInfo(object):

    def __init__(self):
        self._price_money = None
        self._price_text = None
        self._prop_path = None
        self._quantity = None
        self._sku_desc = None
        self._sku_id = None

    @property
    def price_money(self):
        return self._price_money

    @price_money.setter
    def price_money(self, value):
        self._price_money = value
    @property
    def price_text(self):
        return self._price_text

    @price_text.setter
    def price_text(self, value):
        self._price_text = value
    @property
    def prop_path(self):
        return self._prop_path

    @prop_path.setter
    def prop_path(self, value):
        self._prop_path = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def sku_desc(self):
        return self._sku_desc

    @sku_desc.setter
    def sku_desc(self, value):
        self._sku_desc = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.price_money:
            if hasattr(self.price_money, 'to_alipay_dict'):
                params['price_money'] = self.price_money.to_alipay_dict()
            else:
                params['price_money'] = self.price_money
        if self.price_text:
            if hasattr(self.price_text, 'to_alipay_dict'):
                params['price_text'] = self.price_text.to_alipay_dict()
            else:
                params['price_text'] = self.price_text
        if self.prop_path:
            if hasattr(self.prop_path, 'to_alipay_dict'):
                params['prop_path'] = self.prop_path.to_alipay_dict()
            else:
                params['prop_path'] = self.prop_path
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.sku_desc:
            if hasattr(self.sku_desc, 'to_alipay_dict'):
                params['sku_desc'] = self.sku_desc.to_alipay_dict()
            else:
                params['sku_desc'] = self.sku_desc
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
        o = GoodsSkuInfo()
        if 'price_money' in d:
            o.price_money = d['price_money']
        if 'price_text' in d:
            o.price_text = d['price_text']
        if 'prop_path' in d:
            o.prop_path = d['prop_path']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'sku_desc' in d:
            o.sku_desc = d['sku_desc']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        return o


