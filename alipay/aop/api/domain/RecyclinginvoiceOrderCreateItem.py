#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecyclinginvoiceOrderCreateItem(object):

    def __init__(self):
        self._company_item_id = None
        self._item_name = None
        self._item_num = None
        self._item_spec = None
        self._item_total_amount = None
        self._item_unit = None
        self._item_unit_amount = None
        self._tax_code = None

    @property
    def company_item_id(self):
        return self._company_item_id

    @company_item_id.setter
    def company_item_id(self, value):
        self._company_item_id = value
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
    @property
    def item_unit_amount(self):
        return self._item_unit_amount

    @item_unit_amount.setter
    def item_unit_amount(self, value):
        self._item_unit_amount = value
    @property
    def tax_code(self):
        return self._tax_code

    @tax_code.setter
    def tax_code(self, value):
        self._tax_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.company_item_id:
            if hasattr(self.company_item_id, 'to_alipay_dict'):
                params['company_item_id'] = self.company_item_id.to_alipay_dict()
            else:
                params['company_item_id'] = self.company_item_id
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
        if self.item_unit_amount:
            if hasattr(self.item_unit_amount, 'to_alipay_dict'):
                params['item_unit_amount'] = self.item_unit_amount.to_alipay_dict()
            else:
                params['item_unit_amount'] = self.item_unit_amount
        if self.tax_code:
            if hasattr(self.tax_code, 'to_alipay_dict'):
                params['tax_code'] = self.tax_code.to_alipay_dict()
            else:
                params['tax_code'] = self.tax_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecyclinginvoiceOrderCreateItem()
        if 'company_item_id' in d:
            o.company_item_id = d['company_item_id']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_num' in d:
            o.item_num = d['item_num']
        if 'item_spec' in d:
            o.item_spec = d['item_spec']
        if 'item_total_amount' in d:
            o.item_total_amount = d['item_total_amount']
        if 'item_unit' in d:
            o.item_unit = d['item_unit']
        if 'item_unit_amount' in d:
            o.item_unit_amount = d['item_unit_amount']
        if 'tax_code' in d:
            o.tax_code = d['tax_code']
        return o


