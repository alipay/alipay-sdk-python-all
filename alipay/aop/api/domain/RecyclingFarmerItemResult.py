#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecyclingFarmerItemResult(object):

    def __init__(self):
        self._item_num = None
        self._item_unit = None
        self._sale_end_date = None
        self._sale_start_date = None
        self._tax_code = None

    @property
    def item_num(self):
        return self._item_num

    @item_num.setter
    def item_num(self, value):
        self._item_num = value
    @property
    def item_unit(self):
        return self._item_unit

    @item_unit.setter
    def item_unit(self, value):
        self._item_unit = value
    @property
    def sale_end_date(self):
        return self._sale_end_date

    @sale_end_date.setter
    def sale_end_date(self, value):
        self._sale_end_date = value
    @property
    def sale_start_date(self):
        return self._sale_start_date

    @sale_start_date.setter
    def sale_start_date(self, value):
        self._sale_start_date = value
    @property
    def tax_code(self):
        return self._tax_code

    @tax_code.setter
    def tax_code(self, value):
        self._tax_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_num:
            if hasattr(self.item_num, 'to_alipay_dict'):
                params['item_num'] = self.item_num.to_alipay_dict()
            else:
                params['item_num'] = self.item_num
        if self.item_unit:
            if hasattr(self.item_unit, 'to_alipay_dict'):
                params['item_unit'] = self.item_unit.to_alipay_dict()
            else:
                params['item_unit'] = self.item_unit
        if self.sale_end_date:
            if hasattr(self.sale_end_date, 'to_alipay_dict'):
                params['sale_end_date'] = self.sale_end_date.to_alipay_dict()
            else:
                params['sale_end_date'] = self.sale_end_date
        if self.sale_start_date:
            if hasattr(self.sale_start_date, 'to_alipay_dict'):
                params['sale_start_date'] = self.sale_start_date.to_alipay_dict()
            else:
                params['sale_start_date'] = self.sale_start_date
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
        o = RecyclingFarmerItemResult()
        if 'item_num' in d:
            o.item_num = d['item_num']
        if 'item_unit' in d:
            o.item_unit = d['item_unit']
        if 'sale_end_date' in d:
            o.sale_end_date = d['sale_end_date']
        if 'sale_start_date' in d:
            o.sale_start_date = d['sale_start_date']
        if 'tax_code' in d:
            o.tax_code = d['tax_code']
        return o


