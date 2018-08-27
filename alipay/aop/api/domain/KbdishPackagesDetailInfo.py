#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbdishPackagesDetailInfo(object):

    def __init__(self):
        self._detail_count = None
        self._detail_is_select = None
        self._detail_member_price = None
        self._detail_sell_price = None
        self._detail_sku_id = None
        self._detail_sort = None
        self._detail_type = None
        self._group_id = None
        self._packages_sku_id = None

    @property
    def detail_count(self):
        return self._detail_count

    @detail_count.setter
    def detail_count(self, value):
        self._detail_count = value
    @property
    def detail_is_select(self):
        return self._detail_is_select

    @detail_is_select.setter
    def detail_is_select(self, value):
        self._detail_is_select = value
    @property
    def detail_member_price(self):
        return self._detail_member_price

    @detail_member_price.setter
    def detail_member_price(self, value):
        self._detail_member_price = value
    @property
    def detail_sell_price(self):
        return self._detail_sell_price

    @detail_sell_price.setter
    def detail_sell_price(self, value):
        self._detail_sell_price = value
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
    def detail_type(self):
        return self._detail_type

    @detail_type.setter
    def detail_type(self, value):
        self._detail_type = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def packages_sku_id(self):
        return self._packages_sku_id

    @packages_sku_id.setter
    def packages_sku_id(self, value):
        self._packages_sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.detail_count:
            if hasattr(self.detail_count, 'to_alipay_dict'):
                params['detail_count'] = self.detail_count.to_alipay_dict()
            else:
                params['detail_count'] = self.detail_count
        if self.detail_is_select:
            if hasattr(self.detail_is_select, 'to_alipay_dict'):
                params['detail_is_select'] = self.detail_is_select.to_alipay_dict()
            else:
                params['detail_is_select'] = self.detail_is_select
        if self.detail_member_price:
            if hasattr(self.detail_member_price, 'to_alipay_dict'):
                params['detail_member_price'] = self.detail_member_price.to_alipay_dict()
            else:
                params['detail_member_price'] = self.detail_member_price
        if self.detail_sell_price:
            if hasattr(self.detail_sell_price, 'to_alipay_dict'):
                params['detail_sell_price'] = self.detail_sell_price.to_alipay_dict()
            else:
                params['detail_sell_price'] = self.detail_sell_price
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
        if self.detail_type:
            if hasattr(self.detail_type, 'to_alipay_dict'):
                params['detail_type'] = self.detail_type.to_alipay_dict()
            else:
                params['detail_type'] = self.detail_type
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.packages_sku_id:
            if hasattr(self.packages_sku_id, 'to_alipay_dict'):
                params['packages_sku_id'] = self.packages_sku_id.to_alipay_dict()
            else:
                params['packages_sku_id'] = self.packages_sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishPackagesDetailInfo()
        if 'detail_count' in d:
            o.detail_count = d['detail_count']
        if 'detail_is_select' in d:
            o.detail_is_select = d['detail_is_select']
        if 'detail_member_price' in d:
            o.detail_member_price = d['detail_member_price']
        if 'detail_sell_price' in d:
            o.detail_sell_price = d['detail_sell_price']
        if 'detail_sku_id' in d:
            o.detail_sku_id = d['detail_sku_id']
        if 'detail_sort' in d:
            o.detail_sort = d['detail_sort']
        if 'detail_type' in d:
            o.detail_type = d['detail_type']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'packages_sku_id' in d:
            o.packages_sku_id = d['packages_sku_id']
        return o


