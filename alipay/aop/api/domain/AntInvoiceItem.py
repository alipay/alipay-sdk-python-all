#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntInvoiceItem(object):

    def __init__(self):
        self._amount = None
        self._item_name = None
        self._item_no = None
        self._price = None
        self._quantity = None
        self._row_type = None
        self._specification = None
        self._sum_price = None
        self._tax = None
        self._tax_rate = None
        self._unit = None
        self._zero_rate_flag = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def item_no(self):
        return self._item_no

    @item_no.setter
    def item_no(self, value):
        self._item_no = value
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
    def row_type(self):
        return self._row_type

    @row_type.setter
    def row_type(self, value):
        self._row_type = value
    @property
    def specification(self):
        return self._specification

    @specification.setter
    def specification(self, value):
        self._specification = value
    @property
    def sum_price(self):
        return self._sum_price

    @sum_price.setter
    def sum_price(self, value):
        self._sum_price = value
    @property
    def tax(self):
        return self._tax

    @tax.setter
    def tax(self, value):
        self._tax = value
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value
    @property
    def zero_rate_flag(self):
        return self._zero_rate_flag

    @zero_rate_flag.setter
    def zero_rate_flag(self, value):
        self._zero_rate_flag = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.item_no:
            if hasattr(self.item_no, 'to_alipay_dict'):
                params['item_no'] = self.item_no.to_alipay_dict()
            else:
                params['item_no'] = self.item_no
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
        if self.row_type:
            if hasattr(self.row_type, 'to_alipay_dict'):
                params['row_type'] = self.row_type.to_alipay_dict()
            else:
                params['row_type'] = self.row_type
        if self.specification:
            if hasattr(self.specification, 'to_alipay_dict'):
                params['specification'] = self.specification.to_alipay_dict()
            else:
                params['specification'] = self.specification
        if self.sum_price:
            if hasattr(self.sum_price, 'to_alipay_dict'):
                params['sum_price'] = self.sum_price.to_alipay_dict()
            else:
                params['sum_price'] = self.sum_price
        if self.tax:
            if hasattr(self.tax, 'to_alipay_dict'):
                params['tax'] = self.tax.to_alipay_dict()
            else:
                params['tax'] = self.tax
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        if self.unit:
            if hasattr(self.unit, 'to_alipay_dict'):
                params['unit'] = self.unit.to_alipay_dict()
            else:
                params['unit'] = self.unit
        if self.zero_rate_flag:
            if hasattr(self.zero_rate_flag, 'to_alipay_dict'):
                params['zero_rate_flag'] = self.zero_rate_flag.to_alipay_dict()
            else:
                params['zero_rate_flag'] = self.zero_rate_flag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntInvoiceItem()
        if 'amount' in d:
            o.amount = d['amount']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_no' in d:
            o.item_no = d['item_no']
        if 'price' in d:
            o.price = d['price']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'row_type' in d:
            o.row_type = d['row_type']
        if 'specification' in d:
            o.specification = d['specification']
        if 'sum_price' in d:
            o.sum_price = d['sum_price']
        if 'tax' in d:
            o.tax = d['tax']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        if 'unit' in d:
            o.unit = d['unit']
        if 'zero_rate_flag' in d:
            o.zero_rate_flag = d['zero_rate_flag']
        return o


