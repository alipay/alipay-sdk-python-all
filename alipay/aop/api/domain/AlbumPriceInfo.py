#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlbumPriceInfo(object):

    def __init__(self):
        self._actual_price = None
        self._item_id = None
        self._price = None
        self._sell_type = None

    @property
    def actual_price(self):
        return self._actual_price

    @actual_price.setter
    def actual_price(self, value):
        self._actual_price = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def sell_type(self):
        return self._sell_type

    @sell_type.setter
    def sell_type(self, value):
        self._sell_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_price:
            if hasattr(self.actual_price, 'to_alipay_dict'):
                params['actual_price'] = self.actual_price.to_alipay_dict()
            else:
                params['actual_price'] = self.actual_price
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.sell_type:
            if hasattr(self.sell_type, 'to_alipay_dict'):
                params['sell_type'] = self.sell_type.to_alipay_dict()
            else:
                params['sell_type'] = self.sell_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlbumPriceInfo()
        if 'actual_price' in d:
            o.actual_price = d['actual_price']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'price' in d:
            o.price = d['price']
        if 'sell_type' in d:
            o.sell_type = d['sell_type']
        return o


