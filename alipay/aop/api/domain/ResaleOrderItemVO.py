#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ResaleOrderItemVO(object):

    def __init__(self):
        self._item_id = None
        self._item_price = None
        self._item_quantity = None
        self._out_item_id = None
        self._out_item_name = None
        self._out_sku_id = None

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_price(self):
        return self._item_price

    @item_price.setter
    def item_price(self, value):
        self._item_price = value
    @property
    def item_quantity(self):
        return self._item_quantity

    @item_quantity.setter
    def item_quantity(self, value):
        self._item_quantity = value
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value
    @property
    def out_item_name(self):
        return self._out_item_name

    @out_item_name.setter
    def out_item_name(self, value):
        self._out_item_name = value
    @property
    def out_sku_id(self):
        return self._out_sku_id

    @out_sku_id.setter
    def out_sku_id(self, value):
        self._out_sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_price:
            if hasattr(self.item_price, 'to_alipay_dict'):
                params['item_price'] = self.item_price.to_alipay_dict()
            else:
                params['item_price'] = self.item_price
        if self.item_quantity:
            if hasattr(self.item_quantity, 'to_alipay_dict'):
                params['item_quantity'] = self.item_quantity.to_alipay_dict()
            else:
                params['item_quantity'] = self.item_quantity
        if self.out_item_id:
            if hasattr(self.out_item_id, 'to_alipay_dict'):
                params['out_item_id'] = self.out_item_id.to_alipay_dict()
            else:
                params['out_item_id'] = self.out_item_id
        if self.out_item_name:
            if hasattr(self.out_item_name, 'to_alipay_dict'):
                params['out_item_name'] = self.out_item_name.to_alipay_dict()
            else:
                params['out_item_name'] = self.out_item_name
        if self.out_sku_id:
            if hasattr(self.out_sku_id, 'to_alipay_dict'):
                params['out_sku_id'] = self.out_sku_id.to_alipay_dict()
            else:
                params['out_sku_id'] = self.out_sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ResaleOrderItemVO()
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_price' in d:
            o.item_price = d['item_price']
        if 'item_quantity' in d:
            o.item_quantity = d['item_quantity']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        if 'out_item_name' in d:
            o.out_item_name = d['out_item_name']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        return o


