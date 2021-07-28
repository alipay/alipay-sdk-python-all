#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceItemApplyOpenModel(object):

    def __init__(self):
        self._item_ex_tax_amount = None
        self._item_name = None
        self._item_no = None
        self._item_quantity = None
        self._item_spec = None
        self._item_sum_amount = None
        self._item_tax_amount = None
        self._item_tax_rate = None
        self._item_unit = None
        self._item_unit_price = None
        self._prefer_policy_flag = None
        self._row_type = None
        self._special_manage_flag = None
        self._zero_tax_flag = None

    @property
    def item_ex_tax_amount(self):
        return self._item_ex_tax_amount

    @item_ex_tax_amount.setter
    def item_ex_tax_amount(self, value):
        self._item_ex_tax_amount = value
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
    def item_sum_amount(self):
        return self._item_sum_amount

    @item_sum_amount.setter
    def item_sum_amount(self, value):
        self._item_sum_amount = value
    @property
    def item_tax_amount(self):
        return self._item_tax_amount

    @item_tax_amount.setter
    def item_tax_amount(self, value):
        self._item_tax_amount = value
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
    def item_unit_price(self):
        return self._item_unit_price

    @item_unit_price.setter
    def item_unit_price(self, value):
        self._item_unit_price = value
    @property
    def prefer_policy_flag(self):
        return self._prefer_policy_flag

    @prefer_policy_flag.setter
    def prefer_policy_flag(self, value):
        self._prefer_policy_flag = value
    @property
    def row_type(self):
        return self._row_type

    @row_type.setter
    def row_type(self, value):
        self._row_type = value
    @property
    def special_manage_flag(self):
        return self._special_manage_flag

    @special_manage_flag.setter
    def special_manage_flag(self, value):
        self._special_manage_flag = value
    @property
    def zero_tax_flag(self):
        return self._zero_tax_flag

    @zero_tax_flag.setter
    def zero_tax_flag(self, value):
        self._zero_tax_flag = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_ex_tax_amount:
            if hasattr(self.item_ex_tax_amount, 'to_alipay_dict'):
                params['item_ex_tax_amount'] = self.item_ex_tax_amount.to_alipay_dict()
            else:
                params['item_ex_tax_amount'] = self.item_ex_tax_amount
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
        if self.item_sum_amount:
            if hasattr(self.item_sum_amount, 'to_alipay_dict'):
                params['item_sum_amount'] = self.item_sum_amount.to_alipay_dict()
            else:
                params['item_sum_amount'] = self.item_sum_amount
        if self.item_tax_amount:
            if hasattr(self.item_tax_amount, 'to_alipay_dict'):
                params['item_tax_amount'] = self.item_tax_amount.to_alipay_dict()
            else:
                params['item_tax_amount'] = self.item_tax_amount
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
        if self.item_unit_price:
            if hasattr(self.item_unit_price, 'to_alipay_dict'):
                params['item_unit_price'] = self.item_unit_price.to_alipay_dict()
            else:
                params['item_unit_price'] = self.item_unit_price
        if self.prefer_policy_flag:
            if hasattr(self.prefer_policy_flag, 'to_alipay_dict'):
                params['prefer_policy_flag'] = self.prefer_policy_flag.to_alipay_dict()
            else:
                params['prefer_policy_flag'] = self.prefer_policy_flag
        if self.row_type:
            if hasattr(self.row_type, 'to_alipay_dict'):
                params['row_type'] = self.row_type.to_alipay_dict()
            else:
                params['row_type'] = self.row_type
        if self.special_manage_flag:
            if hasattr(self.special_manage_flag, 'to_alipay_dict'):
                params['special_manage_flag'] = self.special_manage_flag.to_alipay_dict()
            else:
                params['special_manage_flag'] = self.special_manage_flag
        if self.zero_tax_flag:
            if hasattr(self.zero_tax_flag, 'to_alipay_dict'):
                params['zero_tax_flag'] = self.zero_tax_flag.to_alipay_dict()
            else:
                params['zero_tax_flag'] = self.zero_tax_flag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceItemApplyOpenModel()
        if 'item_ex_tax_amount' in d:
            o.item_ex_tax_amount = d['item_ex_tax_amount']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_no' in d:
            o.item_no = d['item_no']
        if 'item_quantity' in d:
            o.item_quantity = d['item_quantity']
        if 'item_spec' in d:
            o.item_spec = d['item_spec']
        if 'item_sum_amount' in d:
            o.item_sum_amount = d['item_sum_amount']
        if 'item_tax_amount' in d:
            o.item_tax_amount = d['item_tax_amount']
        if 'item_tax_rate' in d:
            o.item_tax_rate = d['item_tax_rate']
        if 'item_unit' in d:
            o.item_unit = d['item_unit']
        if 'item_unit_price' in d:
            o.item_unit_price = d['item_unit_price']
        if 'prefer_policy_flag' in d:
            o.prefer_policy_flag = d['prefer_policy_flag']
        if 'row_type' in d:
            o.row_type = d['row_type']
        if 'special_manage_flag' in d:
            o.special_manage_flag = d['special_manage_flag']
        if 'zero_tax_flag' in d:
            o.zero_tax_flag = d['zero_tax_flag']
        return o


