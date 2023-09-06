#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InputInvoiceLineRegisterOpenApiDTO(object):

    def __init__(self):
        self._amount = None
        self._currency = None
        self._excluding_tax_amount = None
        self._goods_desc = None
        self._model = None
        self._quantity = None
        self._quantity_unit = None
        self._tax_amount = None
        self._tax_categories = None
        self._tax_rate = None
        self._unit_price = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def excluding_tax_amount(self):
        return self._excluding_tax_amount

    @excluding_tax_amount.setter
    def excluding_tax_amount(self, value):
        self._excluding_tax_amount = value
    @property
    def goods_desc(self):
        return self._goods_desc

    @goods_desc.setter
    def goods_desc(self, value):
        self._goods_desc = value
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def quantity_unit(self):
        return self._quantity_unit

    @quantity_unit.setter
    def quantity_unit(self, value):
        self._quantity_unit = value
    @property
    def tax_amount(self):
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, value):
        self._tax_amount = value
    @property
    def tax_categories(self):
        return self._tax_categories

    @tax_categories.setter
    def tax_categories(self, value):
        self._tax_categories = value
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value
    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        self._unit_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.excluding_tax_amount:
            if hasattr(self.excluding_tax_amount, 'to_alipay_dict'):
                params['excluding_tax_amount'] = self.excluding_tax_amount.to_alipay_dict()
            else:
                params['excluding_tax_amount'] = self.excluding_tax_amount
        if self.goods_desc:
            if hasattr(self.goods_desc, 'to_alipay_dict'):
                params['goods_desc'] = self.goods_desc.to_alipay_dict()
            else:
                params['goods_desc'] = self.goods_desc
        if self.model:
            if hasattr(self.model, 'to_alipay_dict'):
                params['model'] = self.model.to_alipay_dict()
            else:
                params['model'] = self.model
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.quantity_unit:
            if hasattr(self.quantity_unit, 'to_alipay_dict'):
                params['quantity_unit'] = self.quantity_unit.to_alipay_dict()
            else:
                params['quantity_unit'] = self.quantity_unit
        if self.tax_amount:
            if hasattr(self.tax_amount, 'to_alipay_dict'):
                params['tax_amount'] = self.tax_amount.to_alipay_dict()
            else:
                params['tax_amount'] = self.tax_amount
        if self.tax_categories:
            if hasattr(self.tax_categories, 'to_alipay_dict'):
                params['tax_categories'] = self.tax_categories.to_alipay_dict()
            else:
                params['tax_categories'] = self.tax_categories
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        if self.unit_price:
            if hasattr(self.unit_price, 'to_alipay_dict'):
                params['unit_price'] = self.unit_price.to_alipay_dict()
            else:
                params['unit_price'] = self.unit_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InputInvoiceLineRegisterOpenApiDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'currency' in d:
            o.currency = d['currency']
        if 'excluding_tax_amount' in d:
            o.excluding_tax_amount = d['excluding_tax_amount']
        if 'goods_desc' in d:
            o.goods_desc = d['goods_desc']
        if 'model' in d:
            o.model = d['model']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'quantity_unit' in d:
            o.quantity_unit = d['quantity_unit']
        if 'tax_amount' in d:
            o.tax_amount = d['tax_amount']
        if 'tax_categories' in d:
            o.tax_categories = d['tax_categories']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        if 'unit_price' in d:
            o.unit_price = d['unit_price']
        return o


