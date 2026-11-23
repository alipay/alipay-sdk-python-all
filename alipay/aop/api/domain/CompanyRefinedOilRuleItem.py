#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CompanyRefinedOilRuleItem(object):

    def __init__(self):
        self._batch_quantity_l = None
        self._item_tax_code = None

    @property
    def batch_quantity_l(self):
        return self._batch_quantity_l

    @batch_quantity_l.setter
    def batch_quantity_l(self, value):
        self._batch_quantity_l = value
    @property
    def item_tax_code(self):
        return self._item_tax_code

    @item_tax_code.setter
    def item_tax_code(self, value):
        self._item_tax_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_quantity_l:
            if hasattr(self.batch_quantity_l, 'to_alipay_dict'):
                params['batch_quantity_l'] = self.batch_quantity_l.to_alipay_dict()
            else:
                params['batch_quantity_l'] = self.batch_quantity_l
        if self.item_tax_code:
            if hasattr(self.item_tax_code, 'to_alipay_dict'):
                params['item_tax_code'] = self.item_tax_code.to_alipay_dict()
            else:
                params['item_tax_code'] = self.item_tax_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CompanyRefinedOilRuleItem()
        if 'batch_quantity_l' in d:
            o.batch_quantity_l = d['batch_quantity_l']
        if 'item_tax_code' in d:
            o.item_tax_code = d['item_tax_code']
        return o


