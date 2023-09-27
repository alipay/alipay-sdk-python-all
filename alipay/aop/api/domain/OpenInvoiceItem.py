#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenInvoiceItem(object):

    def __init__(self):
        self._item_amount = None
        self._item_name = None
        self._item_num = None
        self._item_spec = None
        self._item_tax_amount = None
        self._item_tax_rate = None
        self._item_total_amount = None
        self._item_unit = None

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
    def item_num(self):
        return self._item_num

    @item_num.setter
    def item_num(self, value):
        self._item_num = value
    @property
    def item_spec(self):
        return self._item_spec

    @item_spec.setter
    def item_spec(self, value):
        self._item_spec = value
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
    def item_total_amount(self):
        return self._item_total_amount

    @item_total_amount.setter
    def item_total_amount(self, value):
        self._item_total_amount = value
    @property
    def item_unit(self):
        return self._item_unit

    @item_unit.setter
    def item_unit(self, value):
        self._item_unit = value


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
        if self.item_num:
            if hasattr(self.item_num, 'to_alipay_dict'):
                params['item_num'] = self.item_num.to_alipay_dict()
            else:
                params['item_num'] = self.item_num
        if self.item_spec:
            if hasattr(self.item_spec, 'to_alipay_dict'):
                params['item_spec'] = self.item_spec.to_alipay_dict()
            else:
                params['item_spec'] = self.item_spec
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
        if self.item_total_amount:
            if hasattr(self.item_total_amount, 'to_alipay_dict'):
                params['item_total_amount'] = self.item_total_amount.to_alipay_dict()
            else:
                params['item_total_amount'] = self.item_total_amount
        if self.item_unit:
            if hasattr(self.item_unit, 'to_alipay_dict'):
                params['item_unit'] = self.item_unit.to_alipay_dict()
            else:
                params['item_unit'] = self.item_unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenInvoiceItem()
        if 'item_amount' in d:
            o.item_amount = d['item_amount']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_num' in d:
            o.item_num = d['item_num']
        if 'item_spec' in d:
            o.item_spec = d['item_spec']
        if 'item_tax_amount' in d:
            o.item_tax_amount = d['item_tax_amount']
        if 'item_tax_rate' in d:
            o.item_tax_rate = d['item_tax_rate']
        if 'item_total_amount' in d:
            o.item_total_amount = d['item_total_amount']
        if 'item_unit' in d:
            o.item_unit = d['item_unit']
        return o


