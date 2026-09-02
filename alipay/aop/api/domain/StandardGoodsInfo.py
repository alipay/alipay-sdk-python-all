#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyDTO import MultiCurrencyMoneyDTO


class StandardGoodsInfo(object):

    def __init__(self):
        self._category = None
        self._goods_id = None
        self._quantity = None
        self._title = None
        self._unit_amount = None

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def unit_amount(self):
        return self._unit_amount

    @unit_amount.setter
    def unit_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyDTO):
            self._unit_amount = value
        else:
            self._unit_amount = MultiCurrencyMoneyDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.unit_amount:
            if hasattr(self.unit_amount, 'to_alipay_dict'):
                params['unit_amount'] = self.unit_amount.to_alipay_dict()
            else:
                params['unit_amount'] = self.unit_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StandardGoodsInfo()
        if 'category' in d:
            o.category = d['category']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'title' in d:
            o.title = d['title']
        if 'unit_amount' in d:
            o.unit_amount = d['unit_amount']
        return o


