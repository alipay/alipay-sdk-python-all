#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceApplyItems(object):

    def __init__(self):
        self._item_amount = None
        self._item_name = None
        self._item_quantity = None
        self._item_spec = None
        self._item_tax_code = None
        self._item_tax_rate = None
        self._item_unit = None
        self._item_unit_amount_with_tax = None

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
    def item_quantity(self):
        return self._item_quantity

    @item_quantity.setter
    def item_quantity(self, value):
        self._item_quantity = value
    @property
    def item_spec(self):
        return self._item_spec

    @item_spec.setter
    def item_spec(self, value):
        self._item_spec = value
    @property
    def item_tax_code(self):
        return self._item_tax_code

    @item_tax_code.setter
    def item_tax_code(self, value):
        self._item_tax_code = value
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
    def item_unit_amount_with_tax(self):
        return self._item_unit_amount_with_tax

    @item_unit_amount_with_tax.setter
    def item_unit_amount_with_tax(self, value):
        self._item_unit_amount_with_tax = value


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
        if self.item_quantity:
            if hasattr(self.item_quantity, 'to_alipay_dict'):
                params['item_quantity'] = self.item_quantity.to_alipay_dict()
            else:
                params['item_quantity'] = self.item_quantity
        if self.item_spec:
            if hasattr(self.item_spec, 'to_alipay_dict'):
                params['item_spec'] = self.item_spec.to_alipay_dict()
            else:
                params['item_spec'] = self.item_spec
        if self.item_tax_code:
            if hasattr(self.item_tax_code, 'to_alipay_dict'):
                params['item_tax_code'] = self.item_tax_code.to_alipay_dict()
            else:
                params['item_tax_code'] = self.item_tax_code
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
        if self.item_unit_amount_with_tax:
            if hasattr(self.item_unit_amount_with_tax, 'to_alipay_dict'):
                params['item_unit_amount_with_tax'] = self.item_unit_amount_with_tax.to_alipay_dict()
            else:
                params['item_unit_amount_with_tax'] = self.item_unit_amount_with_tax
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceApplyItems()
        if 'item_amount' in d:
            o.item_amount = d['item_amount']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_quantity' in d:
            o.item_quantity = d['item_quantity']
        if 'item_spec' in d:
            o.item_spec = d['item_spec']
        if 'item_tax_code' in d:
            o.item_tax_code = d['item_tax_code']
        if 'item_tax_rate' in d:
            o.item_tax_rate = d['item_tax_rate']
        if 'item_unit' in d:
            o.item_unit = d['item_unit']
        if 'item_unit_amount_with_tax' in d:
            o.item_unit_amount_with_tax = d['item_unit_amount_with_tax']
        return o


