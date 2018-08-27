#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecruitItemApplyData(object):

    def __init__(self):
        self._activity_price = None
        self._activity_stock = None
        self._item_id = None
        self._original_price = None
        self._sales = None

    @property
    def activity_price(self):
        return self._activity_price

    @activity_price.setter
    def activity_price(self, value):
        self._activity_price = value
    @property
    def activity_stock(self):
        return self._activity_stock

    @activity_stock.setter
    def activity_stock(self, value):
        self._activity_stock = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, value):
        self._sales = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_price:
            if hasattr(self.activity_price, 'to_alipay_dict'):
                params['activity_price'] = self.activity_price.to_alipay_dict()
            else:
                params['activity_price'] = self.activity_price
        if self.activity_stock:
            if hasattr(self.activity_stock, 'to_alipay_dict'):
                params['activity_stock'] = self.activity_stock.to_alipay_dict()
            else:
                params['activity_stock'] = self.activity_stock
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.sales:
            if hasattr(self.sales, 'to_alipay_dict'):
                params['sales'] = self.sales.to_alipay_dict()
            else:
                params['sales'] = self.sales
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecruitItemApplyData()
        if 'activity_price' in d:
            o.activity_price = d['activity_price']
        if 'activity_stock' in d:
            o.activity_stock = d['activity_stock']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'sales' in d:
            o.sales = d['sales']
        return o


