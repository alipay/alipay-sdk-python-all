#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CartActivityBean(object):

    def __init__(self):
        self._activity_id = None
        self._limit_cnt = None
        self._original_price = None
        self._original_sku_id = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def limit_cnt(self):
        return self._limit_cnt

    @limit_cnt.setter
    def limit_cnt(self, value):
        self._limit_cnt = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def original_sku_id(self):
        return self._original_sku_id

    @original_sku_id.setter
    def original_sku_id(self, value):
        self._original_sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.limit_cnt:
            if hasattr(self.limit_cnt, 'to_alipay_dict'):
                params['limit_cnt'] = self.limit_cnt.to_alipay_dict()
            else:
                params['limit_cnt'] = self.limit_cnt
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.original_sku_id:
            if hasattr(self.original_sku_id, 'to_alipay_dict'):
                params['original_sku_id'] = self.original_sku_id.to_alipay_dict()
            else:
                params['original_sku_id'] = self.original_sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CartActivityBean()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'limit_cnt' in d:
            o.limit_cnt = d['limit_cnt']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'original_sku_id' in d:
            o.original_sku_id = d['original_sku_id']
        return o


