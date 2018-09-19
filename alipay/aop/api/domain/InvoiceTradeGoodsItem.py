#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceTradeGoodsItem(object):

    def __init__(self):
        self._category = None
        self._goods_name = None
        self._goods_no = None
        self._goods_sum_amount = None
        self._price = None
        self._quantity = None
        self._specification = None
        self._unit = None

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def goods_no(self):
        return self._goods_no

    @goods_no.setter
    def goods_no(self, value):
        self._goods_no = value
    @property
    def goods_sum_amount(self):
        return self._goods_sum_amount

    @goods_sum_amount.setter
    def goods_sum_amount(self, value):
        self._goods_sum_amount = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def specification(self):
        return self._specification

    @specification.setter
    def specification(self, value):
        self._specification = value
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.goods_no:
            if hasattr(self.goods_no, 'to_alipay_dict'):
                params['goods_no'] = self.goods_no.to_alipay_dict()
            else:
                params['goods_no'] = self.goods_no
        if self.goods_sum_amount:
            if hasattr(self.goods_sum_amount, 'to_alipay_dict'):
                params['goods_sum_amount'] = self.goods_sum_amount.to_alipay_dict()
            else:
                params['goods_sum_amount'] = self.goods_sum_amount
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.specification:
            if hasattr(self.specification, 'to_alipay_dict'):
                params['specification'] = self.specification.to_alipay_dict()
            else:
                params['specification'] = self.specification
        if self.unit:
            if hasattr(self.unit, 'to_alipay_dict'):
                params['unit'] = self.unit.to_alipay_dict()
            else:
                params['unit'] = self.unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceTradeGoodsItem()
        if 'category' in d:
            o.category = d['category']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'goods_no' in d:
            o.goods_no = d['goods_no']
        if 'goods_sum_amount' in d:
            o.goods_sum_amount = d['goods_sum_amount']
        if 'price' in d:
            o.price = d['price']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'specification' in d:
            o.specification = d['specification']
        if 'unit' in d:
            o.unit = d['unit']
        return o


