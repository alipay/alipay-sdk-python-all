#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PosFixedDishGroupModel(object):

    def __init__(self):
        self._count = None
        self._detail_sku_spec_name = None
        self._detail_sku_unit_name = None
        self._dish_id = None
        self._dish_name = None
        self._group_id = None
        self._sell_price = None
        self._sku_id = None
        self._sort = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def detail_sku_spec_name(self):
        return self._detail_sku_spec_name

    @detail_sku_spec_name.setter
    def detail_sku_spec_name(self, value):
        self._detail_sku_spec_name = value
    @property
    def detail_sku_unit_name(self):
        return self._detail_sku_unit_name

    @detail_sku_unit_name.setter
    def detail_sku_unit_name(self, value):
        self._detail_sku_unit_name = value
    @property
    def dish_id(self):
        return self._dish_id

    @dish_id.setter
    def dish_id(self, value):
        self._dish_id = value
    @property
    def dish_name(self):
        return self._dish_name

    @dish_name.setter
    def dish_name(self, value):
        self._dish_name = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def sell_price(self):
        return self._sell_price

    @sell_price.setter
    def sell_price(self, value):
        self._sell_price = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, value):
        self._sort = value


    def to_alipay_dict(self):
        params = dict()
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.detail_sku_spec_name:
            if hasattr(self.detail_sku_spec_name, 'to_alipay_dict'):
                params['detail_sku_spec_name'] = self.detail_sku_spec_name.to_alipay_dict()
            else:
                params['detail_sku_spec_name'] = self.detail_sku_spec_name
        if self.detail_sku_unit_name:
            if hasattr(self.detail_sku_unit_name, 'to_alipay_dict'):
                params['detail_sku_unit_name'] = self.detail_sku_unit_name.to_alipay_dict()
            else:
                params['detail_sku_unit_name'] = self.detail_sku_unit_name
        if self.dish_id:
            if hasattr(self.dish_id, 'to_alipay_dict'):
                params['dish_id'] = self.dish_id.to_alipay_dict()
            else:
                params['dish_id'] = self.dish_id
        if self.dish_name:
            if hasattr(self.dish_name, 'to_alipay_dict'):
                params['dish_name'] = self.dish_name.to_alipay_dict()
            else:
                params['dish_name'] = self.dish_name
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.sell_price:
            if hasattr(self.sell_price, 'to_alipay_dict'):
                params['sell_price'] = self.sell_price.to_alipay_dict()
            else:
                params['sell_price'] = self.sell_price
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
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
        o = PosFixedDishGroupModel()
        if 'count' in d:
            o.count = d['count']
        if 'detail_sku_spec_name' in d:
            o.detail_sku_spec_name = d['detail_sku_spec_name']
        if 'detail_sku_unit_name' in d:
            o.detail_sku_unit_name = d['detail_sku_unit_name']
        if 'dish_id' in d:
            o.dish_id = d['dish_id']
        if 'dish_name' in d:
            o.dish_name = d['dish_name']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'sell_price' in d:
            o.sell_price = d['sell_price']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'sort' in d:
            o.sort = d['sort']
        return o


