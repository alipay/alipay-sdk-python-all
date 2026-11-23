#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcIndustryinvoiceOilinventoryReturnModel(object):

    def __init__(self):
        self._item_tax_code = None
        self._quantity_l = None
        self._tax_no = None

    @property
    def item_tax_code(self):
        return self._item_tax_code

    @item_tax_code.setter
    def item_tax_code(self, value):
        self._item_tax_code = value
    @property
    def quantity_l(self):
        return self._quantity_l

    @quantity_l.setter
    def quantity_l(self, value):
        self._quantity_l = value
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_tax_code:
            if hasattr(self.item_tax_code, 'to_alipay_dict'):
                params['item_tax_code'] = self.item_tax_code.to_alipay_dict()
            else:
                params['item_tax_code'] = self.item_tax_code
        if self.quantity_l:
            if hasattr(self.quantity_l, 'to_alipay_dict'):
                params['quantity_l'] = self.quantity_l.to_alipay_dict()
            else:
                params['quantity_l'] = self.quantity_l
        if self.tax_no:
            if hasattr(self.tax_no, 'to_alipay_dict'):
                params['tax_no'] = self.tax_no.to_alipay_dict()
            else:
                params['tax_no'] = self.tax_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcIndustryinvoiceOilinventoryReturnModel()
        if 'item_tax_code' in d:
            o.item_tax_code = d['item_tax_code']
        if 'quantity_l' in d:
            o.quantity_l = d['quantity_l']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        return o


