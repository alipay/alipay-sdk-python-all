#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbdishGroupDetailInfo(object):

    def __init__(self):
        self._add_price = None
        self._detail_count = None
        self._detail_dish_id = None
        self._detail_is_default = None
        self._detail_sku_id = None
        self._detail_sort = None
        self._group_id = None

    @property
    def add_price(self):
        return self._add_price

    @add_price.setter
    def add_price(self, value):
        self._add_price = value
    @property
    def detail_count(self):
        return self._detail_count

    @detail_count.setter
    def detail_count(self, value):
        self._detail_count = value
    @property
    def detail_dish_id(self):
        return self._detail_dish_id

    @detail_dish_id.setter
    def detail_dish_id(self, value):
        self._detail_dish_id = value
    @property
    def detail_is_default(self):
        return self._detail_is_default

    @detail_is_default.setter
    def detail_is_default(self, value):
        self._detail_is_default = value
    @property
    def detail_sku_id(self):
        return self._detail_sku_id

    @detail_sku_id.setter
    def detail_sku_id(self, value):
        self._detail_sku_id = value
    @property
    def detail_sort(self):
        return self._detail_sort

    @detail_sort.setter
    def detail_sort(self, value):
        self._detail_sort = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.add_price:
            if hasattr(self.add_price, 'to_alipay_dict'):
                params['add_price'] = self.add_price.to_alipay_dict()
            else:
                params['add_price'] = self.add_price
        if self.detail_count:
            if hasattr(self.detail_count, 'to_alipay_dict'):
                params['detail_count'] = self.detail_count.to_alipay_dict()
            else:
                params['detail_count'] = self.detail_count
        if self.detail_dish_id:
            if hasattr(self.detail_dish_id, 'to_alipay_dict'):
                params['detail_dish_id'] = self.detail_dish_id.to_alipay_dict()
            else:
                params['detail_dish_id'] = self.detail_dish_id
        if self.detail_is_default:
            if hasattr(self.detail_is_default, 'to_alipay_dict'):
                params['detail_is_default'] = self.detail_is_default.to_alipay_dict()
            else:
                params['detail_is_default'] = self.detail_is_default
        if self.detail_sku_id:
            if hasattr(self.detail_sku_id, 'to_alipay_dict'):
                params['detail_sku_id'] = self.detail_sku_id.to_alipay_dict()
            else:
                params['detail_sku_id'] = self.detail_sku_id
        if self.detail_sort:
            if hasattr(self.detail_sort, 'to_alipay_dict'):
                params['detail_sort'] = self.detail_sort.to_alipay_dict()
            else:
                params['detail_sort'] = self.detail_sort
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishGroupDetailInfo()
        if 'add_price' in d:
            o.add_price = d['add_price']
        if 'detail_count' in d:
            o.detail_count = d['detail_count']
        if 'detail_dish_id' in d:
            o.detail_dish_id = d['detail_dish_id']
        if 'detail_is_default' in d:
            o.detail_is_default = d['detail_is_default']
        if 'detail_sku_id' in d:
            o.detail_sku_id = d['detail_sku_id']
        if 'detail_sort' in d:
            o.detail_sort = d['detail_sort']
        if 'group_id' in d:
            o.group_id = d['group_id']
        return o


