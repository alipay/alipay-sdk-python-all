#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceItemContent(object):

    def __init__(self):
        self._item_amount = None
        self._item_name = None
        self._item_no = None
        self._item_price = None
        self._item_quantity = None
        self._item_sum_price = None
        self._item_tax_price = None
        self._item_tax_rate = None
        self._item_unit = None
        self._row_type = None

    @property
    def item_amount(self):
        return self._item_amount

    @item_amount.setter
    def item_amount(self, value):
        self._item_amount = value
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
    def item_price(self):
        return self._item_price

    @item_price.setter
    def item_price(self, value):
        self._item_price = value
    @property
    def item_quantity(self):
        return self._item_quantity

    @item_quantity.setter
    def item_quantity(self, value):
        self._item_quantity = value
    @property
    def item_sum_price(self):
        return self._item_sum_price

    @item_sum_price.setter
    def item_sum_price(self, value):
        self._item_sum_price = value
    @property
    def item_tax_price(self):
        return self._item_tax_price

    @item_tax_price.setter
    def item_tax_price(self, value):
        self._item_tax_price = value
    @property
    def item_tax_rate(self):
        return self._item_tax_rate

    @item_tax_rate.setter
    def item_tax_rate(self, value):
        self._item_tax_rate = value
    @property
    def item_unit(self):
        return self._item_unit

    @item_unit.setter
    def item_unit(self, value):
        self._item_unit = value
    @property
    def row_type(self):
        return self._row_type

    @row_type.setter
    def row_type(self, value):
        self._row_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_amount:
            if hasattr(self.item_amount, 'to_alipay_dict'):
                params['item_amount'] = self.item_amount.to_alipay_dict()
            else:
                params['item_amount'] = self.item_amount
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
        if self.item_price:
            if hasattr(self.item_price, 'to_alipay_dict'):
                params['item_price'] = self.item_price.to_alipay_dict()
            else:
                params['item_price'] = self.item_price
        if self.item_quantity:
            if hasattr(self.item_quantity, 'to_alipay_dict'):
                params['item_quantity'] = self.item_quantity.to_alipay_dict()
            else:
                params['item_quantity'] = self.item_quantity
        if self.item_sum_price:
            if hasattr(self.item_sum_price, 'to_alipay_dict'):
                params['item_sum_price'] = self.item_sum_price.to_alipay_dict()
            else:
                params['item_sum_price'] = self.item_sum_price
        if self.item_tax_price:
            if hasattr(self.item_tax_price, 'to_alipay_dict'):
                params['item_tax_price'] = self.item_tax_price.to_alipay_dict()
            else:
                params['item_tax_price'] = self.item_tax_price
        if self.item_tax_rate:
            if hasattr(self.item_tax_rate, 'to_alipay_dict'):
                params['item_tax_rate'] = self.item_tax_rate.to_alipay_dict()
            else:
                params['item_tax_rate'] = self.item_tax_rate
        if self.item_unit:
            if hasattr(self.item_unit, 'to_alipay_dict'):
                params['item_unit'] = self.item_unit.to_alipay_dict()
            else:
                params['item_unit'] = self.item_unit
        if self.row_type:
            if hasattr(self.row_type, 'to_alipay_dict'):
                params['row_type'] = self.row_type.to_alipay_dict()
            else:
                params['row_type'] = self.row_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceItemContent()
        if 'item_amount' in d:
            o.item_amount = d['item_amount']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_no' in d:
            o.item_no = d['item_no']
        if 'item_price' in d:
            o.item_price = d['item_price']
        if 'item_quantity' in d:
            o.item_quantity = d['item_quantity']
        if 'item_sum_price' in d:
            o.item_sum_price = d['item_sum_price']
        if 'item_tax_price' in d:
            o.item_tax_price = d['item_tax_price']
        if 'item_tax_rate' in d:
            o.item_tax_rate = d['item_tax_rate']
        if 'item_unit' in d:
            o.item_unit = d['item_unit']
        if 'row_type' in d:
            o.row_type = d['row_type']
        return o


