#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MarketingParamBean(object):

    def __init__(self):
        self._item_discount_sku_id = None
        self._limit_cnt = None
        self._origin_sku_id = None

    @property
    def item_discount_sku_id(self):
        return self._item_discount_sku_id

    @item_discount_sku_id.setter
    def item_discount_sku_id(self, value):
        self._item_discount_sku_id = value
    @property
    def limit_cnt(self):
        return self._limit_cnt

    @limit_cnt.setter
    def limit_cnt(self, value):
        self._limit_cnt = value
    @property
    def origin_sku_id(self):
        return self._origin_sku_id

    @origin_sku_id.setter
    def origin_sku_id(self, value):
        self._origin_sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_discount_sku_id:
            if hasattr(self.item_discount_sku_id, 'to_alipay_dict'):
                params['item_discount_sku_id'] = self.item_discount_sku_id.to_alipay_dict()
            else:
                params['item_discount_sku_id'] = self.item_discount_sku_id
        if self.limit_cnt:
            if hasattr(self.limit_cnt, 'to_alipay_dict'):
                params['limit_cnt'] = self.limit_cnt.to_alipay_dict()
            else:
                params['limit_cnt'] = self.limit_cnt
        if self.origin_sku_id:
            if hasattr(self.origin_sku_id, 'to_alipay_dict'):
                params['origin_sku_id'] = self.origin_sku_id.to_alipay_dict()
            else:
                params['origin_sku_id'] = self.origin_sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MarketingParamBean()
        if 'item_discount_sku_id' in d:
            o.item_discount_sku_id = d['item_discount_sku_id']
        if 'limit_cnt' in d:
            o.limit_cnt = d['limit_cnt']
        if 'origin_sku_id' in d:
            o.origin_sku_id = d['origin_sku_id']
        return o


