#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbdishGroupDetailSimplifyInfo(object):

    def __init__(self):
        self._add_price = None
        self._detail_count = None
        self._out_dish_id = None
        self._out_sku_id = None
        self._rule = None
        self._sort = None

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
    def out_dish_id(self):
        return self._out_dish_id

    @out_dish_id.setter
    def out_dish_id(self, value):
        self._out_dish_id = value
    @property
    def out_sku_id(self):
        return self._out_sku_id

    @out_sku_id.setter
    def out_sku_id(self, value):
        self._out_sku_id = value
    @property
    def rule(self):
        return self._rule

    @rule.setter
    def rule(self, value):
        self._rule = value
    @property
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, value):
        self._sort = value


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
        if self.out_dish_id:
            if hasattr(self.out_dish_id, 'to_alipay_dict'):
                params['out_dish_id'] = self.out_dish_id.to_alipay_dict()
            else:
                params['out_dish_id'] = self.out_dish_id
        if self.out_sku_id:
            if hasattr(self.out_sku_id, 'to_alipay_dict'):
                params['out_sku_id'] = self.out_sku_id.to_alipay_dict()
            else:
                params['out_sku_id'] = self.out_sku_id
        if self.rule:
            if hasattr(self.rule, 'to_alipay_dict'):
                params['rule'] = self.rule.to_alipay_dict()
            else:
                params['rule'] = self.rule
        if self.sort:
            if hasattr(self.sort, 'to_alipay_dict'):
                params['sort'] = self.sort.to_alipay_dict()
            else:
                params['sort'] = self.sort
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishGroupDetailSimplifyInfo()
        if 'add_price' in d:
            o.add_price = d['add_price']
        if 'detail_count' in d:
            o.detail_count = d['detail_count']
        if 'out_dish_id' in d:
            o.out_dish_id = d['out_dish_id']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        if 'rule' in d:
            o.rule = d['rule']
        if 'sort' in d:
            o.sort = d['sort']
        return o


