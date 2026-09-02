#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderItemDTO(object):

    def __init__(self):
        self._amount = None
        self._item_id = None
        self._item_image = None
        self._item_name = None
        self._quantity = None
        self._sku_id = None
        self._sku_name = None
        self._unit_price = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_image(self):
        return self._item_image

    @item_image.setter
    def item_image(self, value):
        self._item_image = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def sku_name(self):
        return self._sku_name

    @sku_name.setter
    def sku_name(self, value):
        self._sku_name = value
    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        self._unit_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_image:
            if hasattr(self.item_image, 'to_alipay_dict'):
                params['item_image'] = self.item_image.to_alipay_dict()
            else:
                params['item_image'] = self.item_image
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.sku_name:
            if hasattr(self.sku_name, 'to_alipay_dict'):
                params['sku_name'] = self.sku_name.to_alipay_dict()
            else:
                params['sku_name'] = self.sku_name
        if self.unit_price:
            if hasattr(self.unit_price, 'to_alipay_dict'):
                params['unit_price'] = self.unit_price.to_alipay_dict()
            else:
                params['unit_price'] = self.unit_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderItemDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_image' in d:
            o.item_image = d['item_image']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'sku_name' in d:
            o.sku_name = d['sku_name']
        if 'unit_price' in d:
            o.unit_price = d['unit_price']
        return o


