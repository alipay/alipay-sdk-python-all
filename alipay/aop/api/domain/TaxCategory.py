#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TaxCategory(object):

    def __init__(self):
        self._description = None
        self._item_category_name = None
        self._item_name = None
        self._parent_code = None
        self._tax_code = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def item_category_name(self):
        return self._item_category_name

    @item_category_name.setter
    def item_category_name(self, value):
        self._item_category_name = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def parent_code(self):
        return self._parent_code

    @parent_code.setter
    def parent_code(self, value):
        self._parent_code = value
    @property
    def tax_code(self):
        return self._tax_code

    @tax_code.setter
    def tax_code(self, value):
        self._tax_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.item_category_name:
            if hasattr(self.item_category_name, 'to_alipay_dict'):
                params['item_category_name'] = self.item_category_name.to_alipay_dict()
            else:
                params['item_category_name'] = self.item_category_name
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.parent_code:
            if hasattr(self.parent_code, 'to_alipay_dict'):
                params['parent_code'] = self.parent_code.to_alipay_dict()
            else:
                params['parent_code'] = self.parent_code
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
        o = TaxCategory()
        if 'description' in d:
            o.description = d['description']
        if 'item_category_name' in d:
            o.item_category_name = d['item_category_name']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'parent_code' in d:
            o.parent_code = d['parent_code']
        if 'tax_code' in d:
            o.tax_code = d['tax_code']
        return o


