#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TrafficAirticketOrderDiscountInfo(object):

    def __init__(self):
        self._discount_price = None
        self._item_desc = None
        self._item_id = None
        self._item_name = None
        self._item_source = None

    @property
    def discount_price(self):
        return self._discount_price

    @discount_price.setter
    def discount_price(self, value):
        self._discount_price = value
    @property
    def item_desc(self):
        return self._item_desc

    @item_desc.setter
    def item_desc(self, value):
        self._item_desc = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def item_source(self):
        return self._item_source

    @item_source.setter
    def item_source(self, value):
        self._item_source = value


    def to_alipay_dict(self):
        params = dict()
        if self.discount_price:
            if hasattr(self.discount_price, 'to_alipay_dict'):
                params['discount_price'] = self.discount_price.to_alipay_dict()
            else:
                params['discount_price'] = self.discount_price
        if self.item_desc:
            if hasattr(self.item_desc, 'to_alipay_dict'):
                params['item_desc'] = self.item_desc.to_alipay_dict()
            else:
                params['item_desc'] = self.item_desc
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.item_source:
            if hasattr(self.item_source, 'to_alipay_dict'):
                params['item_source'] = self.item_source.to_alipay_dict()
            else:
                params['item_source'] = self.item_source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TrafficAirticketOrderDiscountInfo()
        if 'discount_price' in d:
            o.discount_price = d['discount_price']
        if 'item_desc' in d:
            o.item_desc = d['item_desc']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_source' in d:
            o.item_source = d['item_source']
        return o


