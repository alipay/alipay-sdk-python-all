#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PaymentGoods(object):

    def __init__(self):
        self._brand = None
        self._category = None
        self._quantity = None
        self._remark = None
        self._title = None
        self._unit_amount = None
        self._unit_currency = None

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
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
        self._unit_amount = value
    @property
    def unit_currency(self):
        return self._unit_currency

    @unit_currency.setter
    def unit_currency(self, value):
        self._unit_currency = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand:
            if hasattr(self.brand, 'to_alipay_dict'):
                params['brand'] = self.brand.to_alipay_dict()
            else:
                params['brand'] = self.brand
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
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
        if self.unit_currency:
            if hasattr(self.unit_currency, 'to_alipay_dict'):
                params['unit_currency'] = self.unit_currency.to_alipay_dict()
            else:
                params['unit_currency'] = self.unit_currency
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaymentGoods()
        if 'brand' in d:
            o.brand = d['brand']
        if 'category' in d:
            o.category = d['category']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'remark' in d:
            o.remark = d['remark']
        if 'title' in d:
            o.title = d['title']
        if 'unit_amount' in d:
            o.unit_amount = d['unit_amount']
        if 'unit_currency' in d:
            o.unit_currency = d['unit_currency']
        return o


