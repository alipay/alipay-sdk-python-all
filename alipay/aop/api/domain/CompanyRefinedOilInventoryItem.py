#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CompanyRefinedOilInventoryItem(object):

    def __init__(self):
        self._downloaded_not_used_quantity_l = None
        self._downloaded_quantity_l = None
        self._in_transit_quantity_l = None
        self._item_category_name = None
        self._item_tax_code = None
        self._lock_flag = None
        self._returnable_quantity_l = None
        self._total_quantity_l = None
        self._usable_quantity_l = None

    @property
    def downloaded_not_used_quantity_l(self):
        return self._downloaded_not_used_quantity_l

    @downloaded_not_used_quantity_l.setter
    def downloaded_not_used_quantity_l(self, value):
        self._downloaded_not_used_quantity_l = value
    @property
    def downloaded_quantity_l(self):
        return self._downloaded_quantity_l

    @downloaded_quantity_l.setter
    def downloaded_quantity_l(self, value):
        self._downloaded_quantity_l = value
    @property
    def in_transit_quantity_l(self):
        return self._in_transit_quantity_l

    @in_transit_quantity_l.setter
    def in_transit_quantity_l(self, value):
        self._in_transit_quantity_l = value
    @property
    def item_category_name(self):
        return self._item_category_name

    @item_category_name.setter
    def item_category_name(self, value):
        self._item_category_name = value
    @property
    def item_tax_code(self):
        return self._item_tax_code

    @item_tax_code.setter
    def item_tax_code(self, value):
        self._item_tax_code = value
    @property
    def lock_flag(self):
        return self._lock_flag

    @lock_flag.setter
    def lock_flag(self, value):
        self._lock_flag = value
    @property
    def returnable_quantity_l(self):
        return self._returnable_quantity_l

    @returnable_quantity_l.setter
    def returnable_quantity_l(self, value):
        self._returnable_quantity_l = value
    @property
    def total_quantity_l(self):
        return self._total_quantity_l

    @total_quantity_l.setter
    def total_quantity_l(self, value):
        self._total_quantity_l = value
    @property
    def usable_quantity_l(self):
        return self._usable_quantity_l

    @usable_quantity_l.setter
    def usable_quantity_l(self, value):
        self._usable_quantity_l = value


    def to_alipay_dict(self):
        params = dict()
        if self.downloaded_not_used_quantity_l:
            if hasattr(self.downloaded_not_used_quantity_l, 'to_alipay_dict'):
                params['downloaded_not_used_quantity_l'] = self.downloaded_not_used_quantity_l.to_alipay_dict()
            else:
                params['downloaded_not_used_quantity_l'] = self.downloaded_not_used_quantity_l
        if self.downloaded_quantity_l:
            if hasattr(self.downloaded_quantity_l, 'to_alipay_dict'):
                params['downloaded_quantity_l'] = self.downloaded_quantity_l.to_alipay_dict()
            else:
                params['downloaded_quantity_l'] = self.downloaded_quantity_l
        if self.in_transit_quantity_l:
            if hasattr(self.in_transit_quantity_l, 'to_alipay_dict'):
                params['in_transit_quantity_l'] = self.in_transit_quantity_l.to_alipay_dict()
            else:
                params['in_transit_quantity_l'] = self.in_transit_quantity_l
        if self.item_category_name:
            if hasattr(self.item_category_name, 'to_alipay_dict'):
                params['item_category_name'] = self.item_category_name.to_alipay_dict()
            else:
                params['item_category_name'] = self.item_category_name
        if self.item_tax_code:
            if hasattr(self.item_tax_code, 'to_alipay_dict'):
                params['item_tax_code'] = self.item_tax_code.to_alipay_dict()
            else:
                params['item_tax_code'] = self.item_tax_code
        if self.lock_flag:
            if hasattr(self.lock_flag, 'to_alipay_dict'):
                params['lock_flag'] = self.lock_flag.to_alipay_dict()
            else:
                params['lock_flag'] = self.lock_flag
        if self.returnable_quantity_l:
            if hasattr(self.returnable_quantity_l, 'to_alipay_dict'):
                params['returnable_quantity_l'] = self.returnable_quantity_l.to_alipay_dict()
            else:
                params['returnable_quantity_l'] = self.returnable_quantity_l
        if self.total_quantity_l:
            if hasattr(self.total_quantity_l, 'to_alipay_dict'):
                params['total_quantity_l'] = self.total_quantity_l.to_alipay_dict()
            else:
                params['total_quantity_l'] = self.total_quantity_l
        if self.usable_quantity_l:
            if hasattr(self.usable_quantity_l, 'to_alipay_dict'):
                params['usable_quantity_l'] = self.usable_quantity_l.to_alipay_dict()
            else:
                params['usable_quantity_l'] = self.usable_quantity_l
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CompanyRefinedOilInventoryItem()
        if 'downloaded_not_used_quantity_l' in d:
            o.downloaded_not_used_quantity_l = d['downloaded_not_used_quantity_l']
        if 'downloaded_quantity_l' in d:
            o.downloaded_quantity_l = d['downloaded_quantity_l']
        if 'in_transit_quantity_l' in d:
            o.in_transit_quantity_l = d['in_transit_quantity_l']
        if 'item_category_name' in d:
            o.item_category_name = d['item_category_name']
        if 'item_tax_code' in d:
            o.item_tax_code = d['item_tax_code']
        if 'lock_flag' in d:
            o.lock_flag = d['lock_flag']
        if 'returnable_quantity_l' in d:
            o.returnable_quantity_l = d['returnable_quantity_l']
        if 'total_quantity_l' in d:
            o.total_quantity_l = d['total_quantity_l']
        if 'usable_quantity_l' in d:
            o.usable_quantity_l = d['usable_quantity_l']
        return o


