#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemPriceUpdateByIsvItemIdParam(object):

    def __init__(self):
        self._isv_item_id = None
        self._price = None

    @property
    def isv_item_id(self):
        return self._isv_item_id

    @isv_item_id.setter
    def isv_item_id(self, value):
        self._isv_item_id = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value


    def to_alipay_dict(self):
        params = dict()
        if self.isv_item_id:
            if hasattr(self.isv_item_id, 'to_alipay_dict'):
                params['isv_item_id'] = self.isv_item_id.to_alipay_dict()
            else:
                params['isv_item_id'] = self.isv_item_id
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemPriceUpdateByIsvItemIdParam()
        if 'isv_item_id' in d:
            o.isv_item_id = d['isv_item_id']
        if 'price' in d:
            o.price = d['price']
        return o


